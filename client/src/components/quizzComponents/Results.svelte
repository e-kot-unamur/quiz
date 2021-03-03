<script>
    export let score = 0;
    export let totalScore = 0;
    export let totalTime = 0;
    export let facts = [];
    export let title = "";
    let emailSend = false;
    let email = "";

    function ValidateEmail()
        {
            var email_format_fn = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
            var include_email = email_format_fn.test(email.trim());
            if(include_email === true)
            {
                return true;
            }
            else
            {
                alert("Veuillez choisir un bon format d'adresse email.");
                return false;
            }
        }

    async function emailClick() {
        if (ValidateEmail(email)){     
            emailSend = true ;
            const response = await fetch('/Results', {
            method: 'POST',
            headers: new Headers({
                'Content-Type': 'application/json',
            }),
            body: JSON.stringify({
                address: email,
                point: score,
                total: totalScore,
                quizname: title,
                timequizz: totalTime
            }),
        })
        }
    }
</script>

<style>
    .results {
        min-height: 60vh;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-direction: column;
    }

    h1 {
        text-align: center;
        color : #8d6f9e;
        margin-bottom: 10px;
    }

    h3 {
        text-align: center;
        color : #8d6f9e;
        margin-bottom: 10px;
        margin-top: 15px;
    }

    .input{
        text-align: center;
        padding : 2%;
    }

    p {
        text-align: center;
    }

    .logoFinishLine {
        margin-top: 10vh;
        width: 150px;
    }

    .btnValidEmail {
        display: inline-block;
        margin-top: 10px;
    }

    .principal {
        margin-top: 10px;
        min-width: 85%;
        padding: 20px 15px;
        font-size: larger;
        background-color: #64b49f;
        color: blanchedalmond;
    }

    .confirmSendEmail {
        font-style: italic;
        color: black;
    }

    .btnFinish {
		font-family: marine, sans-serif;
        font-size: 1.1em;
        font-weight: bold;
        font-style: normal;
		background-color: #8d6f9e;

        margin: 15px auto;
        border-radius: 0px;
        padding: 15px 20px ;
	}

    .logoFinish {
        fill : black;
        width: 25px;
        margin-right: 5px;
    }
</style>

<div class="results">
    <!-- L'email a été envoyé-->
    {#if emailSend} 
        <p class="confirmSendEmail">Votre participation a bien été enregistrée pour l'adresse email : {email}</p>
        <p class="principal"> Vous avez marqué un score de {score}/{totalScore} en un temps total de {totalTime} secondes </p>

        <h3>Voici quelques facts sur le thème du quizz :</h3>
        {#each facts as fact}
            <p class="fw-light">{fact}</p>
        {/each}

        <a href="/"><button class="btnFinish" ><img src="/svg/home.svg" alt="Logo Finish" class="logoFinish"/> Terminer</button></a>

    <!-- Demande de l'adresse email -->
    {:else}
        <img src="/svg/finishLine.svg" alt="Logo ligne d'arrivé" class="logoFinishLine"/>

        <div class="input">
            <h1>Enregistrez votre participation</h1>
            <p>Veuillez entrez votre adresse e-mail afin que nous puissions vous recontacter si vous gagnez le concours : </p>
            <input type="text" bind:value={email}/>
            <span><button class="btnValidEmail" on:click={emailClick}>Valider ma participation</button></span>
        </div>
    {/if}
</div>
