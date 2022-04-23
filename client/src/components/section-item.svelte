<script lang="ts">
    export let className = '';
	export let index: string | number;
	export let title: string;
	export let onClick: () => void;
	export let active: boolean;
</script>

<button
	class={`p-2 rounded-md flex transition-all ${active ? 'bg-white' : 'bg-transparent hover:bg-gray-200'} ${className}`}
	on:click={onClick}
>
	<span class="font-medium mr-1">{index}.</span>
	{title}
</button>
