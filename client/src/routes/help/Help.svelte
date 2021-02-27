<script>
    import * as help from "./Help.json"

function handleClick(){
    location.href = "/IST-MST"
}
</script>

<style>
    h2,p{
        text-align: left;
        font-family: Verdana, Geneva, Tahoma, sans-serif;
    }
    h2{
       font-weight: bold; 
    }

</style>
<div class="card" style="width: 58%; margin: auto; background-color: #D3EAEB;margin-top:7%">
    <div class="card-body">
        <h2>A propos</h2>
        <h5 class="card-text; ">{help.globalhelp}</h5>

        <h2>{help.MCQtitle}</h2>
        <p class="card-text; ">{help.MCQhelp}</p>

        <h2>{help.ToFtitle}</h2>
        <p class="card-text; ">{help.ToFhelp}</p>

        <h2>{help.Coloredtitle}</h2>
        <p class="card-text; ">{help.Coloredhelp}</p>

        <h2>{help.Timedtitle}</h2>
        <p class="card-text; ">{help.Timedhelp}</p>
    </div>
    <form style="margin-left: 75%; margin-top 100%;" action="/IST-MST" method = "POST">
        <label>Adresse e-mail :</label>
        <input type="text" name="address" id="address" placeholder="address">
        <input type="submit" value="suivant">
    </form>
</div>
