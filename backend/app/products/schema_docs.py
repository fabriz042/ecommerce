from drf_spectacular.utils import extend_schema, OpenApiResponse, extend_schema_view

products_list_docs = extend_schema(
    summary="List products",
    description="List all products",
    responses={
        200: OpenApiResponse(description="Products listed successfully"),
        404: OpenApiResponse(description="Products not found")
    }
)

products_retrieve_docs = extend_schema(
    summary="Retrieve product",
    description="Retrieve a single product by its ID",
    responses={
        200: OpenApiResponse(description="Product retrieved successfully"),
        404: OpenApiResponse(description="Product not found")
    }
)

products_destroy_docs = extend_schema(
    summary="Delete product",
    description="Delete a product by its ID",
    responses={
        204: OpenApiResponse(description="Product deleted successfully"),
        404: OpenApiResponse(description="Product not found")
    }
)

product_docs = extend_schema_view(
    list=products_list_docs,
    retrieve=products_retrieve_docs,
    destroy=products_destroy_docs
)
