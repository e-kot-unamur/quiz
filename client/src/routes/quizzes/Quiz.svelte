<!-- Manage a quiz at a time -->
<script>
    export let key  //The id
    export let quiz
</script>

<div class="quiz">
    <div>
        {key}<br>
        {JSON.stringify(quiz)}<br><br>
    </div>
</div>