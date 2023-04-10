    const API = "https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=04c35731a5ee918f014970082a0088b1&page=";
    const moviesList = document.getElementById("liste_films");
    
    let precedent=document.getElementById("pres")
    let suivant=document.getElementById("next")
    const pagination =document.getElementById("current")
    let page=1
    // console.log(liste_films)


// changement de couleur au niveau du vote

  //   function getColor(votes) {
  //     if(votes>= 8){
  //         return 'green'
  //     }else if(votes >= 5){
  //         return "orange"
  //     }else{
  //         return 'red'
  //     }
  // }

    function fetchAPI (){
      moviesList.innerHTML = ''
    fetch(API+page)
    .then(res => res.json())
    .then(data => {
      const movies = data.results;
      console.log(data);
  
      for(let i=0; i<movies.length; i++){
        const movie = movies[i];
        const movieElement = document.createElement("div");
        movieElement.setAttribute('class', "movie")

        const movieImage = document.createElement("img");

        const movieName = document.createElement("h2");

        const movieDescription = document.createElement("p");

        const votes = document.createElement("p");

     
        movieImage.src = `https://image.tmdb.org/t/p/w500${movie.poster_path}`;
        movieName.textContent = movie.title;
        movieDescription.textContent = movie.overview;
        votes.textContent=movie.vote_average

  
        movieElement.appendChild(movieImage);
        movieElement.appendChild(movieName);
        movieElement.appendChild(movieDescription);
        movieElement.appendChild(votes)
        moviesList.appendChild(movieElement);

        pagination.innerText=page
      }
    })}
    fetchAPI ()


//fonction pour changer de pages 
           suivant.addEventListener("click",function(){
            page++
            fetchAPI ()
           })
           precedent.addEventListener("click",function(){
            page--
            fetchAPI ()
           })





    




























































//     const movies = [
//   { 
//     name: "The Shawshank Redemption", 
//     description: "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
//     image: "https://www.gstatic.com/tv/thumb/v22vodart/17420/p17420_v_v8_ak.jpg"
//   },
//   {
//     name: "The Godfather",
//     description: "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
//     image: "https://www.gstatic.com/tv/thumb/v22vodart/1523/p1523_v_v8_ad.jpg"
//   },
//   {
//     name: "The Dark Knight",
//     description: "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.",
//     image: "https://www.gstatic.com/tv/thumb/v22vodart/173378/p173378_v_v8_aa.jpg"
//   }
// ];

// const moviesList = document.getElementById("liste_films");

// for(let i=0; i<movies.length; i++){
//   const movie = movies[i];
//   const movieElement = document.createElement("div");
//   const movieImage = document.createElement("img");
//   const movieName = document.createElement("h2");
//   const movieDescription = document.createElement("p");

//   movieImage.src = movie.image;
//   movieName.textContent = movie.name;
//   movieDescription.textContent = movie.description;

//   movieElement.appendChild(movieImage);
//   movieElement.appendChild(movieName);
//   movieElement.appendChild(movieDescription);

//   moviesList.appendChild(movieElement);
// }

    