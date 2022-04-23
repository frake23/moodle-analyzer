import { writable } from 'svelte/store';
import type { GetQuestionsResponse, GetQuestionResponse } from '../types';

interface QuestionStore {
	selectedQuestionIndex: number;
	questions?: GetQuestionsResponse;
	selectedQuestion?: GetQuestionResponse;
}

export const questionStore = writable<QuestionStore>({
	selectedQuestionIndex: 0
});
