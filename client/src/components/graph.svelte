<script lang="ts">
	import Line from 'svelte-chartjs/src/Line.svelte';
	import Bar from 'svelte-chartjs/src/Bar.svelte';
	import type { GetQuestionResponse } from 'src/types';

	export let question: GetQuestionResponse;
	console.log(question.stats);
	$: data = {
		datasets: [
			{
				label: 'Количество ответов от ответа',
				data: question.stats,
				borderColor: '#0052d6',
				backgroundColor: '#8ab7ff'
			}
		]
	};
</script>

<div>
	{#if question.type === 'number'}
		<Line {data} />
	{:else if question.type === 'variant'}
		<Bar {data} />
	{/if}
</div>
