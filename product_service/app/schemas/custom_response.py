from fastapi.responses import JSONResponse


class CustomResponse(JSONResponse):
    def __init__(
        self,
        status_code=200,
        message="Success",
        data=None,
        exception=None,
    ):
        content = {
            "status": status_code,
            "message": message,
            "data": data,
            "exception": str(exception),
        }
        super().__init__(content=content, status_code=status_code)
