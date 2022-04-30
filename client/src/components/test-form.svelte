<script lang="ts">
	import { browser } from '$app/env';
	import { getTests } from '../helpers';
	import Icon from './icon.svelte';

	let name: string;
	let link: string;
	let files: FileList;

	const onSubmit = async () => {
		if (!files?.length || !name || files[0].type !== 'application/json') return;

		const res = await fetch('/api/test', {
			method: 'POST',
			body: JSON.stringify({ name, link, data: JSON.parse(await files[0].text()) }),
			headers: { 'content-type': 'application/json' }
		});

		if (res.status === 200) {
			toggle();
			getTests();
		}
	};

	let showModal = false;
	let toggle = () => {
		showModal = !showModal;
	};

	$: if (browser) {
		if (showModal) {
			document.body.className = 'overflow-hidden';
		} else {
			document.body.className = '';
		}
	}
</script>

<button class="bg-white rounded-full mb-2 p-2 flex items-center justify-center" on:click={toggle}>
	<Icon name="plus" className="text-green-700" />
</button>
{#if showModal}
	<div
		class="absolute left-0 top-0 h-screen w-screen bg-black bg-opacity-50 z-10 flex justify-center items-center"
	>
		<div class="w-96 rounded-md p-4 bg-white">
			<div class="flex justify-between items-start mb-2">
				<h1 class="text-xl font-medium mb-2">Добавление теста</h1>
				<button on:click={toggle}>
					<Icon name="x" className="w-4 h-4 text-black hover:text-red-500 transition-all" />
				</button>
			</div>
			<div class="flex flex-col gap-2">
				<label class="flex flex-col mb-2">
					<span class="mb-1 text-gray-600">Название теста</span>
					<input
						class="focus:ring border p-1 rounded"
						bind:value={name}
						placeholder="Название теста"
					/>
				</label>
				<label class="flex flex-col mb-2">
					<span class="mb-1 text-gray-600">Ссылка на тест</span>
					<input
						class="focus:ring border p-1 rounded"
						bind:value={link}
						placeholder="Ссылка (необязательно)"
					/>
				</label>
				<input
					class={`block w-full text-sm text-slate-500
                        file:mr-4 file:py-2 file:px-4
                        file:rounded-full file:border-0
                        file:text-sm file:font-semibold
                        file:bg-blue-50 file:text-blue-700
                        hover:file:bg-blue-100
                    `}
					accept="application/json"
					bind:files
					type="file"
					title="Выберите файл"
				/>
				<button
					class="rounded-lg p-2 bg-blue-500 hover:bg-blue-600 transition-all text-white flex items-center justify-center"
					on:click={onSubmit}
				>
					Добавить тест
				</button>
			</div>
		</div>
	</div>
{/if}
