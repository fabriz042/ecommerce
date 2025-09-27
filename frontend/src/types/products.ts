// Interfaces for quick product data
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

export interface PaginatedProducts {
  count: number;
  num_pages: number;
  products: Product[];
}

//Interfaces for detailed product information
import { Tag } from "@/types/tags";
import { Sport} from "@/types/sports";

export interface ProductDetail {
  id: string;
  name: string;
  price: number;
  stock: number;
  description: string;
  slug: string;
  weight: number;
  status: string;
  brand: string;
  category: string;
  series?: string;
  character?: string;
  tags: Tag[];
  sports: Sport[];
  images: ImageData[];
}