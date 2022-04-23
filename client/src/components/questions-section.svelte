<script lang="ts">
	import { questionStore } from '../stores/question-store';
	import { testStore } from '../stores/test-store';

	import Section from './section.svelte';
	import SectionItem from './section-item.svelte';
	import EmptySectionAlert from './empty-section-alert.svelte';

	$: if ($testStore.tests) {
		fetch(`/api/question?test_id=${$testStore.tests[$testStore.selectedTestIndex].test_id}`)
			.then((res) => res.json())
			.then((questions) => {
                console.log(questions)
				$questionStore.questions = questions;
			});
	}
</script>

<Section title="Вопросы" className="col-span-3">
	{#if $questionStore.questions}
		{#each $questionStore.questions as { text, question_id }, i}
			<SectionItem
				className="flex-1"
				index={i + 1}
				active={i === $questionStore.selectedQuestionIndex}
				title={text}
				onClick={() => {
					$questionStore.selectedQuestionIndex = i;
				}}
			/>
		{/each}
	{:else}
		<EmptySectionAlert>Пока нет ни одного вопроса</EmptySectionAlert>
	{/if}
</Section>
