# Top música por decadas
![Alt text](img/decades.jpg?raw=true "Title")  
  
    
## Dataset inicial
### Reading Initial Data.ipynb
 - El dataset inicial se trataba de siete datasets, cada uno de una lista de Spotify enfocada en una década.  
 - Unir los siete datasets con **concat**   
 - Eliminar columnas que no se utilizarán ["bpm", "nrgy", "dB", "live", "acous", "spch", "Number"]  
 - Exportar los datos  
   

## API MusicBrainz
### main.py
 - El mbid (el id del artista) da acceso a la nacionalidad del artista. Al no poder acceder a los datos del artista a través de su nombre, sino sólo a través del mbid. Por lo tanto sólo incluí los id's de los artistas más comunes en el dataset, ya que no había forma de acceder al artista a través del mbid.   
  - Crear el diccionario con el id de los top 10 artistas
  - Incluir el país en el dataframe **alldecades** a través de la función **artist_location**

## Text Report
### Parametros:
   
*year:   
-y (type=int)*   
   
 - 1950  
 - 1960  
 - 1970  
 - 1980  
 - 1990  
 - 2000  
 - 2010  
   
*column: -c   
(type=str)*    
   
 - Artist
 - Genre
 - Country
   
*atribute:   
-a (type=str)*    
  
 - Dance  
 - Positiveness  
 - Popularity  
  
### Uso de los parametros:   
  
*results_by_year*  
Devuelve las Artista/Genero/País más comunes de la década seleccionada.  
  
*atributes*    
Devuelve la media de los atributos Bailabilidad/Positividad/Popularidad ordenados por décadas.  


