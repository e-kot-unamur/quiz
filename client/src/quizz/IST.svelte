<script>
    import QuizzArea from "./QuizzArea.svelte";
</script>

<svelte:head>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/js/bootstrap.bundle.min.js" integrity="sha384-b5kHyXgcpbZJO/tY9Ul7kGkf1S0CWuKcCD38l8YkeH8z8QjE0GmW1gYU5S9FOnJ0" crossorigin="anonymous"></script>
    <link rel="stylesheet" href="https://use.typekit.net/bqg3mtv.css">
</svelte:head>

<style>
    body {
        height: 100vh;
        background-color: #609d9f;
        border : 1px solid #609d9f;
    }



    @keyframes changeColorAndPlaceRectangle {
        0%   {fill:#5EAB82; left:75%; top:70%; height: 95%; transform: rotate(45deg)}
        25%  {left:73%; top:69%;}
        50%  {left:73%; top:69%;}
        75%  {left:73%; top:68%;}
        100% {fill:#64B5A1; left:70%; top:68%; height: 100%; transform: rotate(40deg)}
    }

</style>

<body>
    <QuizzArea/>
</body>