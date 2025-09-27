export interface ImageData {
  image_url: string;
  alt_text: string;
}

export interface Product {
  name: string;
  price: number;
  slug: string;
  status: string;
  images: ImageData[];
}

export interface ProductsData {
  count: number;
  num_pages: number;
  productos: Product[];
}