import { useState, useEffect } from "react";
import { API_URL } from "../config";

// ejemplo real de un proyecto donde me di cuenta
// que no incluye ISP

function Salute() {

    interface Author {
   
        author_name : string;
        author_description : string;
        author_picture : string;
        //author_mail : string;
        //author_github : string;
        //author_linkedin : string;
        //contact_MD : string;
    }

    const [author, setAuthor] = useState<Author | null>(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        const fetchAuthor = async () => {
            try {
                const response = await fetch(
                    `${API_URL}/author`
                );

                if (!response.ok) {
                    throw new Error("Error al obtener datos");
                }

                const data: Author = await response.json();
                setAuthor(data);
            } catch(err) {
                setError("No se pudo cargar el author");
                console.error(err);
            } finally {
                setLoading(false);
            }
        };

        fetchAuthor();
    }, []);

    if (loading) return <p>Cargando...</p>
    if (error) return <p>{error}</p>
    if (!author) return null;

    return(
        <div>
            <h1>{author.author_name}</h1>
            <h1>{author.author_description}</h1>
            <img height="60px" width="60px" src={`${API_URL}${author.author_picture}`}></img>
        </div>
    );
}

export default Salute