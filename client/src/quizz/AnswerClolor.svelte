<script>

    export let color;
    export let checkAnswerColorHandler;

</script>


    <button on:click={() => checkAnswerColorHandler(color)} class="AnswerColor">
        {color}
    </button>



<style>

    

</style>