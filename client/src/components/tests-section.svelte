<script lang="ts">
	import { onMount } from 'svelte';
	import { testStore } from '../stores/test-store';

	import Section from './section.svelte';
	import SectionItem from './section-item.svelte';
	import Icon from './icon.svelte';
	import EmptySectionAlert from './empty-section-alert.svelte';
	import TestForm from './test-form.svelte';

	onMount(async () => {
		const res = await fetch('/api/test');
		const tests = await res.json();

		$testStore.tests = tests;
	});
</script>

<Section title="Тесты" className="col-span-3 gap-2">
	<TestForm />
	{#if $testStore.tests}
		{#each $testStore.tests as { name, link }, i}
			<div class="flex items-center">
				<SectionItem
					className="flex-1"
					index={i + 1}
					active={i === $testStore.selectedTestIndex}
					title={name}
					onClick={() => {
						$testStore.selectedTestIndex = i;
					}}
				/>
				<a href={link}>
					<Icon
						name="external-link"
						className="w-4 h-4 ml-2 text-gray-700 hover:text-blue-600 transition-all"
					/>
				</a>
			</div>
		{/each}
	{:else}
		<EmptySectionAlert>Пока нет ни одного теста</EmptySectionAlert>
	{/if}
</Section>
