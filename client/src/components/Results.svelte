
<script>
   
    
    export let score = 0;
    export let totalScore = 0;
    export let totalTime = 0;
    export let facts = [];
    let email = "";
    
    async function submit(){
        const response = await fetch('/Results', {
        method: 'POST',
        headers: new Headers({
            'Content-Type': 'application/json',
        }),
        body: JSON.stringify({
            address: "basile@gmail.com",
            point: score,
            quizname: "test",
            timequizz: totalTime
        }),
    })
    }
</script>

<style>
    h1{
        text-align: center;
        padding: 10px 0 10px 10px;
    }
    .input{
        text-align: center;
        padding : 2%;
    }
    p{
        text-align: center;
    }

    .results{
        padding: 30px;
    }

</style>


<div class="results">
    
    <h1>Vos résultats</h1>
    <p>Vous avez marqué un score de  {score}/{totalScore} </p>
    <p>Vous avez répondu en un total de {totalTime} secondes </p>
    
    <div class="input">
        <p>Veuillez entrez votre adresse e-mail afin que nous puissions vous recontacter si vous gagnez le concours : </p>
        <input type="text" value={email}/>
        <span><button on:click={submit}>Valider</button></span>
    </div>
        
    <h1>Facts </h1>
    <p>Voici quelques facts sur le thème de quizz qui pourraient vous intéressez !</p>
    
    {#each facts as fact}
        <p>{fact}</p>
    {/each}
</div>