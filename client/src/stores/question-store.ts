import { writable } from 'svelte/store';
import type { GetQuestionsResponse } from '../types';

interface QuestionStore {
	selectedQuestionIndex: number;
	questions?: GetQuestionsResponse;
}

export const questionStore = writable<QuestionStore>({
	selectedQuestionIndex: 0
});
