import type { RequestHandler } from '@sveltejs/kit';

export const get: RequestHandler = async (event) => {
	const res = await fetch(`${import.meta.env.VITE_HOST}/question${event.url.search}`);
	const questions = await res.json();

	return {
		body: questions
	};
};
