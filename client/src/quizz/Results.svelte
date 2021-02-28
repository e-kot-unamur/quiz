
<script>
    import Navbar from "./Navbar.svelte"
    
    export let points = 0;
    let email = "";
</script>

<style>
    h1{
        text-align: center;
    }
    input{
        padding-left:10px;
    }
</style>


<div class="results">
    <Navbar/>
    <h1>Vos résultats</h1>
    <span>Vos points : {points} </span>
    
    <p>Veuillez entrez votre adresse e-mail afin que nous puissions vous recontacter si vous gagnez le concours : </p>
    <form style="margin-left: 75%; margin-top 100%;" action="/Results" method = "POST">
    <input type="text" name="address" id="address" placeholder="addresse mail" value={email}>
    <input type="submit" value="suivant">
    </form>
    <span>{email}</span>
</div>
