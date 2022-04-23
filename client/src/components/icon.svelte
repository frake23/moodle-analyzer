<script lang="ts">
	import feather from 'feather-icons';

	export let className: string = '';
	export let name: string;

	$: icon = feather.icons[name];
</script>

{#if icon}
	<svg {...icon.attrs} class={className}>
		<g>
			{@html icon.contents}
		</g>
	</svg>
{/if}
