from drf_spectacular.utils import extend_schema, OpenApiResponse

products_list_docs = extend_schema(
    summary="List products",
    description="List all products",
    responses={
        200: OpenApiResponse(description="Products listed successfully"),
        404: OpenApiResponse(description="Products not found")
    }
)
