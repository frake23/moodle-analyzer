<script lang="ts">
	import { questionStore } from '../stores/question-store';
	import { testStore } from '../stores/test-store';
	import type { GetQuestionResponse } from '../types';
	import Section from './section.svelte';
	import EmptySectionAlert from './empty-section-alert.svelte';
	import Graph from './graph.svelte';

	let question: GetQuestionResponse;

	const getQuestionType = (questionType: GetQuestionResponse['type']) => {
		switch (questionType) {
			case 'variant':
				return 'С выбором варианта';
			case 'text':
				return 'Текстовый вопрос';
			case 'number':
				return 'Числовой вопрос';
		}
	};

	$: if ($testStore.tests?.length && $questionStore.questions?.length) {
		const testId = $testStore.tests[$testStore.selectedTestIndex].test_id;
		const questionId = $questionStore.questions[$questionStore.selectedQuestionIndex].question_id;

		fetch(`/api/question/${questionId}?test_id=${testId}`)
			.then((res) => res.json())
			.then((q) => {
				question = q;
			});
	}
</script>

<Section title="Статистика" className="col-span-6">
	{#if question}
		<div class="flex flex-col">
			<h2 class="font-semibold text-lg">Тип вопроса</h2>
			<div class="mb-2">{getQuestionType(question.type)}</div>
			<h2 class="font-semibold text-lg">Текст вопроса</h2>
			<div class="mb-2 ">{question.text}</div>
			{#if question.stats}
				<h2 class="font-semibold text-lg">График</h2>
				<Graph {question} />
			{:else}
				<h2 class="font-semibold text-lg">Графика нет</h2>
			{/if}
		</div>
	{:else}
		<EmptySectionAlert>Вопрос не выбран</EmptySectionAlert>
	{/if}
</Section>
