// app/page.tsx (o cualquier componente de página)
"use client";

import {
  Carousel,
  CarouselContent,
  CarouselItem,
  CarouselPrevious,
  CarouselNext,
} from "@/components/ui/carousel";
import Image from "next/image";
import {
  Accordion,
  AccordionContent,
  AccordionItem,
  AccordionTrigger,
} from "@/components/ui/accordion"

export default function Home() {
  return (
    <div className="mx-auto">
      {/*Carousel*/}
      <Carousel className="w-full">
        <CarouselContent className="h-[800px]">
          <CarouselItem className="min-w-full relative flex items-center justify-center text-white text-2xl">
              <Image
                src="/balls.jpg"
                alt="Logo"
                fill
                style={{ objectFit: 'cover', filter: 'blur(8px)'  }} // 'cover' si quieres que llene todo el contenedor
              />
              <div className="absolute z-10">
                <div className="z-10">
                  xx
                </div>
                <div className="z-10">
                  <Image
                    src="/productoPelota.png"
                    alt="Pelota"
                    width={150}
                    height={150}
                  />
                </div>
              </div>
          </CarouselItem>
          <CarouselItem className="min-w-full bg-red-500 flex items-center justify-center text-white text-2xl">
            Slide 2
          </CarouselItem>
          <CarouselItem className="min-w-full bg-green-500 flex items-center justify-center text-white text-2xl">
            Slide 3
          </CarouselItem>
        </CarouselContent>
        <CarouselPrevious className="absolute left-50 top-1/2 -translate-y-1/2 p-2 text-white" variant="ghost"/>
        <CarouselNext className="absolute right-50 top-1/2 -translate-y-1/2 p-2 text-white" variant="ghost"/>
      </Carousel>
      {/*Accordeon*/}
      <div className="h-[200px]">
        <Accordion type="single" collapsible>
        <AccordionItem value="item-1">
          <AccordionTrigger>Is it accessible?</AccordionTrigger>
          <AccordionContent>
            Yes. It adheres to the WAI-ARIA design pattern.
          </AccordionContent>
        </AccordionItem>
        </Accordion>
        <Accordion type="single" collapsible>
          <AccordionItem value="item-2">
            <AccordionTrigger>Is it accessible?</AccordionTrigger>
            <AccordionContent>
              Yes. It adheres to the WAI-ARIA design pattern.
            </AccordionContent>
          </AccordionItem>
        </Accordion>
      </div> 
    </div>
  );
}
