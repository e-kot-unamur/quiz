<script>
    import Navbar from '../../components/Navbar.svelte';
    import * as about from './About.json'
</script>
<style>
    h2,p{
        text-align: left;
        margin-left: 15px;
        margin-right: 15px;
    }
    h1{
        padding: 10px 0 20px;
        text-decoration: underline;
        text-align: center;

    }
    h2{
        padding: 10px 0 10px;
        text-decoration: underline;
        font-style: italic;
    }   
    .about{
        /* Verticial align */
		margin: 50px auto auto auto; 
		background-color: #D3EAEB;
		padding : 20px 45px ;
		width : 90%;
    }
    
</style>

<svelte:head>
    <link rel="stylesheet" href="hack.css">
</svelte:head>

<Navbar/>
<div class="about">
    
    <h1>{about.title1}</h1>

    <h2>{about.title2}</h2>
    <p>{about.text1}</p>

    <h2>{about.title3}</h2>
    <p>{about.text1}</p>

    <h2>{about.title4}</h2>
    <p>{about.text3}</p>
</div>
    