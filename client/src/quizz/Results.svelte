
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
    <input type="text" value={email}/>
    <span>{email}</span>
</div>
