# AI Workflow

This is an AI-powered workflow using CrewAI agents to accomplish complex tasks through collaboration.

## Workflow Steps

1. **analyze_laboratory_results_part1**: Create baseline lab analysis framework
2. **analyze_laboratory_results_part2**: Generate hypothesis correlation from lab data
3. **collect_present_symptoms_part1**: Systemic symptom inventory
4. **collect_present_symptoms_part2**: Symptom system mapping
5. **gather_patient_history_part1**: Primary history compilation
6. **gather_patient_history_part2**: History pattern recognition
7. **generate_history_hypotheses_part1**: Baseline hypothesis generation (using output from gather_patient_history_part2)
8. **generate_history_hypotheses_part2**: Hypothesis validation framework (using output from gather_patient_history_part2)
9. **generate_symptom_hypotheses_part1**: Symptom differential framework (using output from collect_present_symptoms_part2)
10. **generate_symptom_hypotheses_part2**: Symptom pattern validation (using output from collect_present_symptoms_part2)
11. **merge_initial_hypotheses_part1**: Baseline hypothesis consolidation (using output from generate_symptom_hypotheses_part2, generate_history_hypotheses_part1)
12. **merge_initial_hypotheses_part2**: Hypothesis decision validation (using output from generate_symptom_hypotheses_part2, generate_history_hypotheses_part1)
13. **categorize_initial_approach_part1**: Define core approach classification (using output from merge_initial_hypotheses_part2)
14. **categorize_initial_approach_part2**: Evaluate approach implementation requirements (using output from merge_initial_hypotheses_part2)
15. **prioritize_diagnostic_tests_part1**: Core test hierarchy creation (using output from merge_initial_hypotheses_part2)
16. **prioritize_diagnostic_tests_part2**: Test cost-effectiveness optimization (using output from merge_initial_hypotheses_part2)
17. **order_imaging_studies_part1**: Primary imaging protocol selection (using output from prioritize_diagnostic_tests_part2)
18. **order_imaging_studies_part2**: Imaging protocol optimization (using output from prioritize_diagnostic_tests_part2)
19. **order_laboratory_tests_part1**: Core lab test protocol design (using output from prioritize_diagnostic_tests_part2)
20. **order_laboratory_tests_part2**: Lab protocol validation (using output from prioritize_diagnostic_tests_part2)
21. **prepare_specialist_referrals_part1**: Core referral framework (using output from prioritize_diagnostic_tests_part2)
22. **prepare_specialist_referrals_part2**: Referral timing optimization (using output from prioritize_diagnostic_tests_part2)
23. **compile_specialist_input_part1**: Structural input synthesis (using output from prepare_specialist_referrals_part2)
24. **compile_specialist_input_part2**: Input validation reconciliation (using output from prepare_specialist_referrals_part2)
25. **review_imaging_findings_part1**: Primary imaging analysis (using output from order_imaging_studies_part2)
26. **review_imaging_findings_part2**: Imaging pathway validation (using output from order_imaging_studies_part2)
27. **update_differential_diagnosis_part1**: Primary differential refinement (using output from analyze_laboratory_results_part1, review_imaging_findings_part1, compile_specialist_input_part1)
28. **update_differential_diagnosis_part2**: Differential decision validation (using output from analyze_laboratory_results_part2, review_imaging_findings_part2, compile_specialist_input_part2)
29. **categorize_diagnostic_pathway_part1**: Establish primary pathway classification (using output from update_differential_diagnosis_part2)
30. **categorize_diagnostic_pathway_part2**: Quantify pathway validation parameters (using output from update_differential_diagnosis_part2)
31. **generate_diagnostic_summary_part1**: Primary conclusion framework (using output from update_differential_diagnosis_part2, categorize_diagnostic_pathway_part1)
32. **generate_diagnostic_summary_part2**: Diagnostic support validation (using output from update_differential_diagnosis_part2, categorize_diagnostic_pathway_part1)
33. **request_confirmatory_testing_part1**: Primary confirmation strategy (using output from generate_diagnostic_summary_part2)
34. **request_confirmatory_testing_part2**: Test validation framework (using output from generate_diagnostic_summary_part2)
35. **finalize_diagnostic_conclusion_part1**: Core conclusion documentation (using output from generate_diagnostic_summary_part2, request_confirmatory_testing_part2)
36. **finalize_diagnostic_conclusion_part2**: Diagnostic path validation (using output from generate_diagnostic_summary_part2, request_confirmatory_testing_part2)

## Running the Workflow

This workflow is self-contained and requires minimal setup:

1. Install uv if you haven't already:
```bash
pip install uv
```

2. Set your OpenAI API key:
```bash
export OPENAI_API_KEY='your-api-key'
```

3. Run the workflow:
```bash
./run.sh
```

That's it! The workflow will automatically handle all dependencies and execution.

## Input/Output

- The workflow accepts input as either plain text or JSON
- Each agent processes its input and produces structured output
- Final results are displayed for each step of the workflow
