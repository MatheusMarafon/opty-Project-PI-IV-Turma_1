import { useState } from "react";
import { ChevronDown, ChevronUp, ExternalLink, Smartphone } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { Card, CardContent } from "@/components/ui/card";

interface Offer {
  store: string;
  price: number;
  condition: string;
  shipping: string;
  link: string;
}

interface ProductCardProps {
  name: string;
  image?: string;
  offers: Offer[];
}

const ProductCard = ({ name, image, offers }: ProductCardProps) => {
  const [isExpanded, setIsExpanded] = useState(false);
  const lowestPrice = Math.min(...offers.map((o) => o.price));

  return (
    <Card className="glass hover-lift">
      <CardContent className="p-6">
        <div className="flex flex-col sm:flex-row gap-4">
          {/* Product Image */}
          <div className="w-full sm:w-32 h-32 bg-gradient-subtle rounded-lg flex items-center justify-center flex-shrink-0">
            {image ? (
              <img src={image} alt={name} className="w-full h-full object-contain rounded-lg" />
            ) : (
              <Smartphone className="h-16 w-16 text-primary/40" />
            )}
          </div>

          {/* Product Info */}
          <div className="flex-1">
            <div className="flex items-start justify-between gap-4 mb-3">
              <h3 className="text-lg font-semibold text-foreground">{name}</h3>
              <Badge variant="default" className="whitespace-nowrap">
                {offers.length} {offers.length === 1 ? "oferta" : "ofertas"}
              </Badge>
            </div>

            <div className="mb-4">
              <div className="text-sm text-muted-foreground mb-1">A partir de:</div>
              <div className="text-3xl font-bold gradient-text">
                {lowestPrice.toLocaleString("pt-BR", { style: "currency", currency: "BRL" })}
              </div>
            </div>

            <Button
              variant="outline"
              onClick={() => setIsExpanded(!isExpanded)}
              className="w-full sm:w-auto"
            >
              {isExpanded ? (
                <>
                  Ocultar Ofertas <ChevronUp className="ml-2 h-4 w-4" />
                </>
              ) : (
                <>
                  Ver Todas as Ofertas <ChevronDown className="ml-2 h-4 w-4" />
                </>
              )}
            </Button>
          </div>
        </div>

        {/* Offers Table */}
        {isExpanded && (
          <div className="mt-6 animate-fade-in">
            <div className="border border-border rounded-lg overflow-hidden">
              <div className="overflow-x-auto">
                <table className="w-full">
                  <thead className="bg-muted/50">
                    <tr>
                      <th className="text-left p-3 text-sm font-semibold">Loja</th>
                      <th className="text-left p-3 text-sm font-semibold">Preço</th>
                      <th className="text-left p-3 text-sm font-semibold hidden sm:table-cell">
                        Condição
                      </th>
                      <th className="text-left p-3 text-sm font-semibold hidden md:table-cell">
                        Frete
                      </th>
                      <th className="text-right p-3 text-sm font-semibold">Ação</th>
                    </tr>
                  </thead>
                  <tbody>
                    {offers.map((offer, index) => {
                      const isLowest = offer.price === lowestPrice;
                      return (
                        <tr
                          key={index}
                          className={`border-t border-border hover:bg-muted/20 transition-colors ${
                            isLowest ? "bg-accent/5" : ""
                          }`}
                        >
                          <td className="p-3">
                            <div className="flex items-center gap-2">
                              <span className="font-medium">{offer.store}</span>
                              {isLowest && (
                                <Badge variant="default" className="bg-accent text-xs">
                                  Melhor Preço
                                </Badge>
                              )}
                            </div>
                          </td>
                          <td className="p-3">
                            <span className="font-semibold text-foreground">
                              {offer.price.toLocaleString("pt-BR", {
                                style: "currency",
                                currency: "BRL",
                              })}
                            </span>
                          </td>
                          <td className="p-3 text-muted-foreground hidden sm:table-cell">
                            {offer.condition}
                          </td>
                          <td className="p-3 hidden md:table-cell">
                            <span
                              className={
                                offer.shipping === "Grátis"
                                  ? "text-accent font-medium"
                                  : "text-muted-foreground"
                              }
                            >
                              {offer.shipping}
                            </span>
                          </td>
                          <td className="p-3 text-right">
                            <Button
                              size="sm"
                              variant="gradient"
                              onClick={() => window.open(offer.link, "_blank")}
                            >
                              Ver Oferta
                              <ExternalLink className="ml-1 h-3 w-3" />
                            </Button>
                          </td>
                        </tr>
                      );
                    })}
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        )}
      </CardContent>
    </Card>
  );
};

export default ProductCard;
