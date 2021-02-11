<script>
    import * as help from "./Help.json"

function handleClick(){
    location.href = "/IST-MST/1"
}
</script>

<style>
    h1,h2,p{
        text-align: left;
        margin-left: 15%;
        margin-right: 15%;
    }
    button{
        margin-left: 85%;
    }
</style>
<p style="font-size:20px">{help.globalhelp}</p>

<h2>{help.MCQtitle}</h2>
<p>{help.MCQhelp}</p>

<h2>{help.ToFtitle}</h2>
<p>{help.ToFhelp}</p>

<h2>{help.Coloredtitle}</h2>
<p>{help.Coloredhelp}</p>

<h2>{help.Timedtitle}</h2>
<p>{help.Timedhelp}</p>

<button on:click={handleClick}>
    Suivant
</button>