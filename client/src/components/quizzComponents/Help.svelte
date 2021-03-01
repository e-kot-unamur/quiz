<script>
    import * as help from "./Help.json"
</script>

<style>
    p, h2 {
        display: inline-block;
        vertical-align: middle;
        text-align: center;
    }

    .section {
        margin-left: 30px;
    }

    h1 {
        text-align: center;
        color : #8d6f9e;
        margin-bottom: 10px;
    }

    @media (max-width : 720px) {
        .section {
            margin-left: 0;
        }
        .logo {
            visibility: hidden;
        }
    }
</style>

<!-- Titre et intro -->
<h1>Quizz.e-kot : présentation du Quizz</h1>
<p style="font-size:20px; text-align:center;">{help.globalhelp}</p>

<!-- Type 1 : question carrées -->
<hr />
<div class="section">
    <img src="/svg/multipleChoice.svg" alt="Logo E-kot" class="logo" width="50px"/>
    <h2>{help.MCQtitle}</h2>
    <p>{help.MCQhelp}</p>
</div>

<!-- Type 2 : Vrai ou Faux -->
<hr />
<div class="section">
    <img src="/svg/trueOrFalse.svg" alt="Logo E-kot" class="logo" width="50px"/>
    <h2>{help.ToFtitle}</h2>
    <p>{help.ToFhelp}</p>
</div>

<!-- Type 3 : Question ° de justesse -->
<hr />
<div class="section">
    <img src="/svg/degre.svg" alt="Logo E-kot" class="logo" width="50px"/>
    <h2>{help.Coloredtitle}</h2>
    <p>{help.Coloredhelp}</p>
</div>

<!-- Type 4 : Timer  -->
<hr />
<div class="section">
    <img src="/svg/timer.svg" alt="Logo E-kot" class="logo" width="50px"/>
    <h2>{help.Timedtitle}</h2>
    <p>{help.Timedhelp}</p>
</div>
