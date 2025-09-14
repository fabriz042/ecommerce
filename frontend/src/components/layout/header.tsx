import Image from "next/image";
import SearchBar from "@/components/ui/Busqueda";
import { AiOutlineUser } from "react-icons/ai";
import { MdFavoriteBorder } from "react-icons/md";

export default function Header() {
    return (
        <header className="justify-center flex top-0">
            <div className="flex fixed space-x-5 z-50 items-center">
                {/*Logo*/}
                <div>
                    <Image src="/logo.png" alt="Logo" width={150} height={150}/>
                </div>
                {/*Menu Categorias*/}
                <div className="flex space-x-5">
                    <div>
                        <h1 className="text-xl">Categorias</h1>
                    </div>
                    <div>
                        <h1 className="text-xl">Promociones</h1>
                    </div>
                    <div>
                        <h1 className="text-xl">Blog</h1>
                    </div>
                </div>
                {/*Barra Busqueda*/}
                <div>
                <SearchBar />
                </div>
                {/*Menu Usuario*/}
                <div className="flex space-x-2">
                    <AiOutlineUser className="h-10 w-10"/>
                    <MdFavoriteBorder className="h-10 w-10"/>
                </div>            
            </div>
        </header>
    );
}
