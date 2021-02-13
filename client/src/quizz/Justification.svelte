<script>
    export let justification;
    export let goodAnswer;
</script>


{#if justification != "" && goodAnswer} 
    <div class="alert alert-success mt-3" role="alert">
        {justification}
    </div>
{:else if justification != ""} 
    <div class="alert alert-danger mt-3" role="alert">
        {justification}
    </div>
{/if}




<style>

</style>

