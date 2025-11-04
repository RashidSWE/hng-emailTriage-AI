from fastapi import APIRouter, HTTPException, Request
from ..models.models import A2ARequest, A2AResponse, EmailInput
from ..agent.agent import email_agent

router = APIRouter(prefix="/a2a")

@router.post("/analyze-email", response_model=A2AResponse)
async def get_agent(request: A2ARequest):
    """ A2A-compatible endpoint so other agents can call this one """
    try:
        result = await email_agent.run(request.input.model_dump())

        output_data = (
            result.output.model_dump()
            if hasattr(result.output, "model_dump")
            else result.output
        )

        tokens_used = 0
        if isinstance(result.usage, dict):
            tokens_used = result.usage.get("total_tokens", 0)
        response = A2AResponse(
            output=output_data,
            usage={"model": "gemini-1.5-flash", "tokens_used": tokens_used},
            status="success"
        )

        return response
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Agent error: {str(e)}"
        )


@router.post("/analyze-email-direct")
async def analyze_email(email: EmailInput):
    try:
        prompt_text = f"""
            From: {email.sender}
            Body: {email.body}
            """
        result = await email_agent.run(prompt_text)
        return result.output
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Agent error ; {str(e)}"
        )


@router.post("/jsonrpc")
async def jsonrpc_endpoint(request: Request):
    try:
        data = await request.json()

        if data.get("jsonrpc") != "2.0":
            raise HTTPException(
                status_code=400,
                detail="Invalid JSON-RPC version. Expected '2.0'"
            )
        
        method = data.get("method")
        params = data.get("params")
        rpc_id = data.get("id")

        
        if method == "analyze_email":
            a2a_request = A2ARequest(**params)

            email_data = a2a_request.input
            prompt_text = f"From: {email_data.sender}\nBody: {email_data.body}"
            result = await email_agent.run(prompt_text)


            output_data = (
                result.output.model_dump()
                if hasattr(result.output, "model_dump")
                else result.output
            )
    
            usage_info = getattr(result, "usage", {}) or {}
            tokens_used = usage_info.get("total_tokens", 0) if isinstance(usage_info, dict) else 0

            a2a_response = A2AResponse(
                output=output_data,
                usage={"model": "gemini-1.5-flash", "tokens_used": tokens_used},
                status="success"
            )
            rpc_result = a2a_response.model_dump()
        else:
            return{
                "jsonrpc": "2.0",
                "error": {"code": -32601, "message": f"Method `{method}` not found"},
                "id": rpc_id
            }
        return {
            "jsonrpc": "2.0",
            "result": rpc_result,
            "id": rpc_id
        }
    except Exception as e:
        return {
            "jonsrpc": "2.0",
            "error": {"code": -32603, "message": f"Internal error: {str(e)}"}
        }
