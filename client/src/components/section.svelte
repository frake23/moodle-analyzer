<script lang="ts">
	export let className = '';
	export let title: string;
</script>

<div class={`flex flex-col rounded-lg p-3  bg-gray-100 ${className}`}>
    <h1 class="text-xl font-bold mb-2">{title}</h1>
    <slot></slot>
</div>
