<script lang="ts">
	import { questionStore } from '../stores/question-store';
	import { testStore } from '../stores/test-store';

	import Section from './section.svelte';
	import SectionItem from './section-item.svelte';
	import EmptySectionAlert from './empty-section-alert.svelte';

	$: if ($testStore.tests?.length) {
		fetch(`/api/question?test_id=${$testStore.tests[$testStore.selectedTestIndex].test_id}`)
			.then((res) => res.json())
			.then((questions) => {
				$questionStore.questions = questions;
			});
	}

	$: {
		$testStore.selectedTestIndex;
		$questionStore.selectedQuestionIndex = 0;
	}
</script>

<Section title="Вопросы" className="col-span-3 gap-2">
	{#if $questionStore.questions}
		{#each $questionStore.questions as { text }, i}
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
