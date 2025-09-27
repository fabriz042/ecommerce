import api from "@/services/api.service";

interface Busqueda {
  search: string;
  limit?: number;
  page?: number | 1;
  estado?: number;
  marca?: string;
}

export const getSearchResults = async ({
  search,
  limit,
  estado,
  page,
}: Busqueda) => {
  try {
    const params = new URLSearchParams();
    params.append("search", search);
    if (limit) params.append("limit", limit.toString());
    if (estado) params.append("estado", estado.toString());
    if (page) params.append("page", page.toString());

    const response = await api.get(`products/?${params.toString()}`);
    return response.data;
  } catch (error) {
    console.error("Error to fetch search results", error);
    throw error;
  }
};

export const getDetalles = async (slug: string) => {
  try {
    const response = await api.get(`products/${slug}`);
    return response.data;
  } catch (error) {
    console.error("Error to fetch product details", error);
    throw error;
  }
};
