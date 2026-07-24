import { configureStore, createSlice } from '@reduxjs/toolkit';

const complaintSlice = createSlice({
  name: 'complaint',
  initialState: {
    formData: {
      complaintSource: 'Email',
      customerName: '',
      productName: '',
      productStrength: '',
      batchNumber: '',
      affectedQuantity: '',
      manufacturingDate: '',
      expiryDate: '',
      originatingSiteBlock: '',
      impactedNPM: '',
      complaintCategory: '',
      complaintDescription: '',
      severity: '',
      suggestedNextAction: '',
      initialRiskAssessment: ''
    },
    statusBadge: 'Pending Triage',
    messages: []
  },
  reducers: {
    updateFormData: (state, action) => {
      state.formData = { ...state.formData, ...action.payload };
      state.statusBadge = 'Ready to Commit';
    },
    addMessage: (state, action) => {
      state.messages.push(action.payload);
    }
  }
});

export const { updateFormData, addMessage } = complaintSlice.actions;

export const store = configureStore({
  reducer: {
    complaint: complaintSlice.reducer
  }
});