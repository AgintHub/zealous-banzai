# /// script
# dependencies = ["crewai==0.105.0"]
# ///
import sys
import logging
from crewai import Crew
from crews import *

class FilteredStream:
    # @traceable
    def __init__(self, original_stream):
        self.original_stream = original_stream
        self.filtered_messages = [
            "File not found:",
            "agents.yaml",
            "tasks.yaml"
        ]
        self.buffer = ""

    # @traceable
    def write(self, text):
        # Add to buffer
        self.buffer += text

        # If we have a complete line (ends with newline)
        if '\n' in self.buffer:
            lines = self.buffer.split('\n')
            # Process all complete lines
            for line in lines[:-1]:
                if not any(msg in line for msg in self.filtered_messages):
                    self.original_stream.write(line + '\n')
            # Keep the last incomplete line in buffer
            self.buffer = lines[-1]

    # @traceable
    def flush(self):
        # Process any remaining buffer content
        if self.buffer and not any(msg in self.buffer for msg in self.filtered_messages):
            self.original_stream.write(self.buffer)
        self.buffer = ""
        self.original_stream.flush()

# Redirect stdout to our filtered stream
sys.stdout = FilteredStream(sys.stdout)

# Suppress CrewAI configuration warnings
logging.basicConfig(level=logging.ERROR)
logging.getLogger().setLevel(logging.ERROR)
import os
import asyncio
from typing import Dict
from crewai import Crew

from crews.analyze_laboratory_results_part1_crew import analyze_laboratory_results_part1_crew
from crews.analyze_laboratory_results_part2_crew import analyze_laboratory_results_part2_crew
from crews.categorize_diagnostic_pathway_part1_crew import categorize_diagnostic_pathway_part1_crew
from crews.categorize_diagnostic_pathway_part2_crew import categorize_diagnostic_pathway_part2_crew
from crews.categorize_initial_approach_part1_crew import categorize_initial_approach_part1_crew
from crews.categorize_initial_approach_part2_crew import categorize_initial_approach_part2_crew
from crews.collect_present_symptoms_part1_crew import collect_present_symptoms_part1_crew
from crews.collect_present_symptoms_part2_crew import collect_present_symptoms_part2_crew
from crews.compile_specialist_input_part1_crew import compile_specialist_input_part1_crew
from crews.compile_specialist_input_part2_crew import compile_specialist_input_part2_crew
from crews.finalize_diagnostic_conclusion_part1_crew import finalize_diagnostic_conclusion_part1_crew
from crews.finalize_diagnostic_conclusion_part2_crew import finalize_diagnostic_conclusion_part2_crew
from crews.gather_patient_history_part1_crew import gather_patient_history_part1_crew
from crews.gather_patient_history_part2_crew import gather_patient_history_part2_crew
from crews.generate_diagnostic_summary_part1_crew import generate_diagnostic_summary_part1_crew
from crews.generate_diagnostic_summary_part2_crew import generate_diagnostic_summary_part2_crew
from crews.generate_history_hypotheses_part1_crew import generate_history_hypotheses_part1_crew
from crews.generate_history_hypotheses_part2_crew import generate_history_hypotheses_part2_crew
from crews.generate_symptom_hypotheses_part1_crew import generate_symptom_hypotheses_part1_crew
from crews.generate_symptom_hypotheses_part2_crew import generate_symptom_hypotheses_part2_crew
from crews.merge_initial_hypotheses_part1_crew import merge_initial_hypotheses_part1_crew
from crews.merge_initial_hypotheses_part2_crew import merge_initial_hypotheses_part2_crew
from crews.order_imaging_studies_part1_crew import order_imaging_studies_part1_crew
from crews.order_imaging_studies_part2_crew import order_imaging_studies_part2_crew
from crews.order_laboratory_tests_part1_crew import order_laboratory_tests_part1_crew
from crews.order_laboratory_tests_part2_crew import order_laboratory_tests_part2_crew
from crews.prepare_specialist_referrals_part1_crew import prepare_specialist_referrals_part1_crew
from crews.prepare_specialist_referrals_part2_crew import prepare_specialist_referrals_part2_crew
from crews.prioritize_diagnostic_tests_part1_crew import prioritize_diagnostic_tests_part1_crew
from crews.prioritize_diagnostic_tests_part2_crew import prioritize_diagnostic_tests_part2_crew
from crews.request_confirmatory_testing_part1_crew import request_confirmatory_testing_part1_crew
from crews.request_confirmatory_testing_part2_crew import request_confirmatory_testing_part2_crew
from crews.review_imaging_findings_part1_crew import review_imaging_findings_part1_crew
from crews.review_imaging_findings_part2_crew import review_imaging_findings_part2_crew
from crews.update_differential_diagnosis_part1_crew import update_differential_diagnosis_part1_crew
from crews.update_differential_diagnosis_part2_crew import update_differential_diagnosis_part2_crew


# @traceable
async def run_workflow(inputs: Dict = None, openai_api_key: str = None):
    """Execute the full workflow."""
    if openai_api_key:
        os.environ["OPENAI_API_KEY"] = openai_api_key
    elif not os.getenv("OPENAI_API_KEY"):
        raise ValueError("OpenAI API key must be provided")

    if inputs is None:
        inputs = {}

    results = {}
    crews = {}
    crews["analyze_laboratory_results_part1"] = analyze_laboratory_results_part1_crew().crew()
    crews["analyze_laboratory_results_part2"] = analyze_laboratory_results_part2_crew().crew()
    crews["categorize_diagnostic_pathway_part1"] = categorize_diagnostic_pathway_part1_crew().crew()
    crews["categorize_diagnostic_pathway_part2"] = categorize_diagnostic_pathway_part2_crew().crew()
    crews["categorize_initial_approach_part1"] = categorize_initial_approach_part1_crew().crew()
    crews["categorize_initial_approach_part2"] = categorize_initial_approach_part2_crew().crew()
    crews["collect_present_symptoms_part1"] = collect_present_symptoms_part1_crew().crew()
    crews["collect_present_symptoms_part2"] = collect_present_symptoms_part2_crew().crew()
    crews["compile_specialist_input_part1"] = compile_specialist_input_part1_crew().crew()
    crews["compile_specialist_input_part2"] = compile_specialist_input_part2_crew().crew()
    crews["finalize_diagnostic_conclusion_part1"] = finalize_diagnostic_conclusion_part1_crew().crew()
    crews["finalize_diagnostic_conclusion_part2"] = finalize_diagnostic_conclusion_part2_crew().crew()
    crews["gather_patient_history_part1"] = gather_patient_history_part1_crew().crew()
    crews["gather_patient_history_part2"] = gather_patient_history_part2_crew().crew()
    crews["generate_diagnostic_summary_part1"] = generate_diagnostic_summary_part1_crew().crew()
    crews["generate_diagnostic_summary_part2"] = generate_diagnostic_summary_part2_crew().crew()
    crews["generate_history_hypotheses_part1"] = generate_history_hypotheses_part1_crew().crew()
    crews["generate_history_hypotheses_part2"] = generate_history_hypotheses_part2_crew().crew()
    crews["generate_symptom_hypotheses_part1"] = generate_symptom_hypotheses_part1_crew().crew()
    crews["generate_symptom_hypotheses_part2"] = generate_symptom_hypotheses_part2_crew().crew()
    crews["merge_initial_hypotheses_part1"] = merge_initial_hypotheses_part1_crew().crew()
    crews["merge_initial_hypotheses_part2"] = merge_initial_hypotheses_part2_crew().crew()
    crews["order_imaging_studies_part1"] = order_imaging_studies_part1_crew().crew()
    crews["order_imaging_studies_part2"] = order_imaging_studies_part2_crew().crew()
    crews["order_laboratory_tests_part1"] = order_laboratory_tests_part1_crew().crew()
    crews["order_laboratory_tests_part2"] = order_laboratory_tests_part2_crew().crew()
    crews["prepare_specialist_referrals_part1"] = prepare_specialist_referrals_part1_crew().crew()
    crews["prepare_specialist_referrals_part2"] = prepare_specialist_referrals_part2_crew().crew()
    crews["prioritize_diagnostic_tests_part1"] = prioritize_diagnostic_tests_part1_crew().crew()
    crews["prioritize_diagnostic_tests_part2"] = prioritize_diagnostic_tests_part2_crew().crew()
    crews["request_confirmatory_testing_part1"] = request_confirmatory_testing_part1_crew().crew()
    crews["request_confirmatory_testing_part2"] = request_confirmatory_testing_part2_crew().crew()
    crews["review_imaging_findings_part1"] = review_imaging_findings_part1_crew().crew()
    crews["review_imaging_findings_part2"] = review_imaging_findings_part2_crew().crew()
    crews["update_differential_diagnosis_part1"] = update_differential_diagnosis_part1_crew().crew()
    crews["update_differential_diagnosis_part2"] = update_differential_diagnosis_part2_crew().crew()

    # Level 0 execution
    results["analyze_laboratory_results_part1"] = await crews["analyze_laboratory_results_part1"].kickoff_async(inputs=inputs)
    results["analyze_laboratory_results_part2"] = await crews["analyze_laboratory_results_part2"].kickoff_async(inputs=inputs)
    results["collect_present_symptoms_part1"] = await crews["collect_present_symptoms_part1"].kickoff_async(inputs=inputs)
    results["collect_present_symptoms_part2"] = await crews["collect_present_symptoms_part2"].kickoff_async(inputs=inputs)
    results["gather_patient_history_part1"] = await crews["gather_patient_history_part1"].kickoff_async(inputs=inputs)
    results["gather_patient_history_part2"] = await crews["gather_patient_history_part2"].kickoff_async(inputs=inputs)

    # Level 1 execution
    level_results = await asyncio.gather(crews["generate_history_hypotheses_part1"].kickoff_async(inputs={"gather_patient_history_part2_output": results["gather_patient_history_part2"].raw}), crews["generate_history_hypotheses_part2"].kickoff_async(inputs={"gather_patient_history_part2_output": results["gather_patient_history_part2"].raw}), crews["generate_symptom_hypotheses_part1"].kickoff_async(inputs={"collect_present_symptoms_part2_output": results["collect_present_symptoms_part2"].raw}), crews["generate_symptom_hypotheses_part2"].kickoff_async(inputs={"collect_present_symptoms_part2_output": results["collect_present_symptoms_part2"].raw}))
    for node_name, result in zip(['generate_history_hypotheses_part1', 'generate_history_hypotheses_part2', 'generate_symptom_hypotheses_part1', 'generate_symptom_hypotheses_part2'], level_results):
        results[node_name] = result

    # Level 2 execution
    level_results = await asyncio.gather(crews["merge_initial_hypotheses_part1"].kickoff_async(inputs={"generate_symptom_hypotheses_part2_output": results["generate_symptom_hypotheses_part2"].raw, "generate_history_hypotheses_part1_output": results["generate_history_hypotheses_part1"].raw}), crews["merge_initial_hypotheses_part2"].kickoff_async(inputs={"generate_symptom_hypotheses_part2_output": results["generate_symptom_hypotheses_part2"].raw, "generate_history_hypotheses_part1_output": results["generate_history_hypotheses_part1"].raw}))
    for node_name, result in zip(['merge_initial_hypotheses_part1', 'merge_initial_hypotheses_part2'], level_results):
        results[node_name] = result

    # Level 3 execution
    level_results = await asyncio.gather(crews["categorize_initial_approach_part1"].kickoff_async(inputs={"merge_initial_hypotheses_part2_output": results["merge_initial_hypotheses_part2"].raw}), crews["categorize_initial_approach_part2"].kickoff_async(inputs={"merge_initial_hypotheses_part2_output": results["merge_initial_hypotheses_part2"].raw}), crews["prioritize_diagnostic_tests_part1"].kickoff_async(inputs={"merge_initial_hypotheses_part2_output": results["merge_initial_hypotheses_part2"].raw}), crews["prioritize_diagnostic_tests_part2"].kickoff_async(inputs={"merge_initial_hypotheses_part2_output": results["merge_initial_hypotheses_part2"].raw}))
    for node_name, result in zip(['categorize_initial_approach_part1', 'categorize_initial_approach_part2', 'prioritize_diagnostic_tests_part1', 'prioritize_diagnostic_tests_part2'], level_results):
        results[node_name] = result

    # Level 4 execution
    level_results = await asyncio.gather(crews["order_imaging_studies_part1"].kickoff_async(inputs={"prioritize_diagnostic_tests_part2_output": results["prioritize_diagnostic_tests_part2"].raw}), crews["order_imaging_studies_part2"].kickoff_async(inputs={"prioritize_diagnostic_tests_part2_output": results["prioritize_diagnostic_tests_part2"].raw}), crews["order_laboratory_tests_part1"].kickoff_async(inputs={"prioritize_diagnostic_tests_part2_output": results["prioritize_diagnostic_tests_part2"].raw}), crews["order_laboratory_tests_part2"].kickoff_async(inputs={"prioritize_diagnostic_tests_part2_output": results["prioritize_diagnostic_tests_part2"].raw}), crews["prepare_specialist_referrals_part1"].kickoff_async(inputs={"prioritize_diagnostic_tests_part2_output": results["prioritize_diagnostic_tests_part2"].raw}), crews["prepare_specialist_referrals_part2"].kickoff_async(inputs={"prioritize_diagnostic_tests_part2_output": results["prioritize_diagnostic_tests_part2"].raw}))
    for node_name, result in zip(['order_imaging_studies_part1', 'order_imaging_studies_part2', 'order_laboratory_tests_part1', 'order_laboratory_tests_part2', 'prepare_specialist_referrals_part1', 'prepare_specialist_referrals_part2'], level_results):
        results[node_name] = result

    # Level 5 execution
    level_results = await asyncio.gather(crews["compile_specialist_input_part1"].kickoff_async(inputs={"prepare_specialist_referrals_part2_output": results["prepare_specialist_referrals_part2"].raw}), crews["compile_specialist_input_part2"].kickoff_async(inputs={"prepare_specialist_referrals_part2_output": results["prepare_specialist_referrals_part2"].raw}), crews["review_imaging_findings_part1"].kickoff_async(inputs={"order_imaging_studies_part2_output": results["order_imaging_studies_part2"].raw}), crews["review_imaging_findings_part2"].kickoff_async(inputs={"order_imaging_studies_part2_output": results["order_imaging_studies_part2"].raw}))
    for node_name, result in zip(['compile_specialist_input_part1', 'compile_specialist_input_part2', 'review_imaging_findings_part1', 'review_imaging_findings_part2'], level_results):
        results[node_name] = result

    # Level 6 execution
    level_results = await asyncio.gather(crews["update_differential_diagnosis_part1"].kickoff_async(inputs={"analyze_laboratory_results_part1_output": results["analyze_laboratory_results_part1"].raw, "review_imaging_findings_part1_output": results["review_imaging_findings_part1"].raw, "compile_specialist_input_part1_output": results["compile_specialist_input_part1"].raw}), crews["update_differential_diagnosis_part2"].kickoff_async(inputs={"analyze_laboratory_results_part2_output": results["analyze_laboratory_results_part2"].raw, "review_imaging_findings_part2_output": results["review_imaging_findings_part2"].raw, "compile_specialist_input_part2_output": results["compile_specialist_input_part2"].raw}))
    for node_name, result in zip(['update_differential_diagnosis_part1', 'update_differential_diagnosis_part2'], level_results):
        results[node_name] = result

    # Level 7 execution
    level_results = await asyncio.gather(crews["categorize_diagnostic_pathway_part1"].kickoff_async(inputs={"update_differential_diagnosis_part2_output": results["update_differential_diagnosis_part2"].raw}), crews["categorize_diagnostic_pathway_part2"].kickoff_async(inputs={"update_differential_diagnosis_part2_output": results["update_differential_diagnosis_part2"].raw}))
    for node_name, result in zip(['categorize_diagnostic_pathway_part1', 'categorize_diagnostic_pathway_part2'], level_results):
        results[node_name] = result

    # Level 8 execution
    level_results = await asyncio.gather(crews["generate_diagnostic_summary_part1"].kickoff_async(inputs={"update_differential_diagnosis_part2_output": results["update_differential_diagnosis_part2"].raw, "categorize_diagnostic_pathway_part1_output": results["categorize_diagnostic_pathway_part1"].raw}), crews["generate_diagnostic_summary_part2"].kickoff_async(inputs={"update_differential_diagnosis_part2_output": results["update_differential_diagnosis_part2"].raw, "categorize_diagnostic_pathway_part1_output": results["categorize_diagnostic_pathway_part1"].raw}))
    for node_name, result in zip(['generate_diagnostic_summary_part1', 'generate_diagnostic_summary_part2'], level_results):
        results[node_name] = result

    # Level 9 execution
    level_results = await asyncio.gather(crews["request_confirmatory_testing_part1"].kickoff_async(inputs={"generate_diagnostic_summary_part2_output": results["generate_diagnostic_summary_part2"].raw}), crews["request_confirmatory_testing_part2"].kickoff_async(inputs={"generate_diagnostic_summary_part2_output": results["generate_diagnostic_summary_part2"].raw}))
    for node_name, result in zip(['request_confirmatory_testing_part1', 'request_confirmatory_testing_part2'], level_results):
        results[node_name] = result

    # Level 10 execution
    level_results = await asyncio.gather(crews["finalize_diagnostic_conclusion_part1"].kickoff_async(inputs={"generate_diagnostic_summary_part2_output": results["generate_diagnostic_summary_part2"].raw, "request_confirmatory_testing_part2_output": results["request_confirmatory_testing_part2"].raw}), crews["finalize_diagnostic_conclusion_part2"].kickoff_async(inputs={"generate_diagnostic_summary_part2_output": results["generate_diagnostic_summary_part2"].raw, "request_confirmatory_testing_part2_output": results["request_confirmatory_testing_part2"].raw}))
    for node_name, result in zip(['finalize_diagnostic_conclusion_part1', 'finalize_diagnostic_conclusion_part2'], level_results):
        results[node_name] = result

    return results

# @traceable
def run_workflow_sync(inputs: Dict = None, openai_api_key: str = None):
    """Synchronous version of run_workflow."""
    return asyncio.run(run_workflow(inputs, openai_api_key))

if __name__ == "__main__":
    import sys
    import json

    api_key = os.getenv("OPENAI_API_KEY") or (sys.argv[1] if len(sys.argv) > 1 else None)
    if not api_key:
        print("Please provide OpenAI API key")
        sys.exit(1)

    print("Provide any runtime inputs/params/args/context in raw text or JSON format (press Enter for empty input):")
    user_input = input().strip()

    inputs = {"input": user_input} if user_input else {}

    try:
        if user_input:
            # Try to parse as JSON if provided
            json_input = json.loads(user_input)
            inputs = {"input": json_input}
    except json.JSONDecodeError:
        # If not valid JSON, use the raw string
        pass

    results = run_workflow_sync(inputs, openai_api_key=api_key)
