import os
import asyncio
import functools
import inspect
import json
import sys
from typing import Dict, Any, List, Callable, Coroutine, Union, Optional

from code.address_fda_comments_and_questions import address_fda_comments_and_questions
from code.clarify_device_type import clarify_device_type
from code.develop_device_documentation import develop_device_documentation
from code.identify_required_fda_submissions import identify_required_fda_submissions
from code.obtain_fda_clearance_or_approval import obtain_fda_clearance_or_approval
from code.perform_competitive_analysis import perform_competitive_analysis
from code.prepare_fda_submission_package import prepare_fda_submission_package
from code.research_fda_regulations import research_fda_regulations
from code.submit_fda_application import submit_fda_application
from code.track_fda_review_progress import track_fda_review_progress

# Get async mode from environment variable or default to False
ASYNC_MODE = os.environ.get('ASYNC_MODE', '').lower() in ('true', '1', 'yes', 'y')

def make_async(func):
    """Convert a synchronous function to an asynchronous function.

    If the function is already asynchronous, return it unchanged.
    If the function is synchronous, wrap it in an async function.
    """
    # If it's already a coroutine function, return it as is
    if inspect.iscoroutinefunction(func):
        return func

    # Otherwise, wrap it as an async function
    @functools.wraps(func)
    async def async_wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return async_wrapper

address_fda_comments_and_questions_async = make_async(address_fda_comments_and_questions)
clarify_device_type_async = make_async(clarify_device_type)
develop_device_documentation_async = make_async(develop_device_documentation)
identify_required_fda_submissions_async = make_async(identify_required_fda_submissions)
obtain_fda_clearance_or_approval_async = make_async(obtain_fda_clearance_or_approval)
perform_competitive_analysis_async = make_async(perform_competitive_analysis)
prepare_fda_submission_package_async = make_async(prepare_fda_submission_package)
research_fda_regulations_async = make_async(research_fda_regulations)
submit_fda_application_async = make_async(submit_fda_application)
track_fda_review_progress_async = make_async(track_fda_review_progress)

async def run_workflow(user_input: str) -> Dict[str, Any]:
    """Execute the workflow by running each level in the topological sort.

    Args:
        user_input: The input string for the workflow

    Returns:
        Dict containing all results keyed by node name
    """
    # Store results for each node
    results = {}

    # Level 0: clarify_device_type
    async def run_clarify_device_type():
        # Call the async version of clarify_device_type with results from dependencies
        return await clarify_device_type_async(user_input)

    # Run level 0 nodes in parallel
    results['clarify_device_type'] = await run_clarify_device_type()

    # Level 1: research_fda_regulations
    async def run_research_fda_regulations():
        # Call the async version of research_fda_regulations with results from dependencies
        return await research_fda_regulations_async(results['clarify_device_type'])

    # Run level 1 nodes in parallel
    results['research_fda_regulations'] = await run_research_fda_regulations()

    # Level 2: perform_competitive_analysis
    async def run_perform_competitive_analysis():
        # Call the async version of perform_competitive_analysis with results from dependencies
        return await perform_competitive_analysis_async(results['research_fda_regulations'])

    # Run level 2 nodes in parallel
    results['perform_competitive_analysis'] = await run_perform_competitive_analysis()

    # Level 3: develop_device_documentation
    async def run_develop_device_documentation():
        # Call the async version of develop_device_documentation with results from dependencies
        return await develop_device_documentation_async(results['research_fda_regulations'], results['perform_competitive_analysis'])

    # Run level 3 nodes in parallel
    results['develop_device_documentation'] = await run_develop_device_documentation()

    # Level 4: identify_required_fda_submissions
    async def run_identify_required_fda_submissions():
        # Call the async version of identify_required_fda_submissions with results from dependencies
        return await identify_required_fda_submissions_async(results['research_fda_regulations'], results['develop_device_documentation'])

    # Run level 4 nodes in parallel
    results['identify_required_fda_submissions'] = await run_identify_required_fda_submissions()

    # Level 5: prepare_fda_submission_package
    async def run_prepare_fda_submission_package():
        # Call the async version of prepare_fda_submission_package with results from dependencies
        return await prepare_fda_submission_package_async(results['identify_required_fda_submissions'], results['develop_device_documentation'])

    # Run level 5 nodes in parallel
    results['prepare_fda_submission_package'] = await run_prepare_fda_submission_package()

    # Level 6: submit_fda_application
    async def run_submit_fda_application():
        # Call the async version of submit_fda_application with results from dependencies
        return await submit_fda_application_async(results['prepare_fda_submission_package'])

    # Run level 6 nodes in parallel
    results['submit_fda_application'] = await run_submit_fda_application()

    # Level 7: track_fda_review_progress
    async def run_track_fda_review_progress():
        # Call the async version of track_fda_review_progress with results from dependencies
        return await track_fda_review_progress_async(results['submit_fda_application'])

    # Run level 7 nodes in parallel
    results['track_fda_review_progress'] = await run_track_fda_review_progress()

    # Level 8: address_fda_comments_and_questions
    async def run_address_fda_comments_and_questions():
        # Call the async version of address_fda_comments_and_questions with results from dependencies
        return await address_fda_comments_and_questions_async(results['track_fda_review_progress'])

    # Run level 8 nodes in parallel
    results['address_fda_comments_and_questions'] = await run_address_fda_comments_and_questions()

    # Level 9: obtain_fda_clearance_or_approval
    async def run_obtain_fda_clearance_or_approval():
        # Call the async version of obtain_fda_clearance_or_approval with results from dependencies
        return await obtain_fda_clearance_or_approval_async(results['address_fda_comments_and_questions'])

    # Run level 9 nodes in parallel
    results['obtain_fda_clearance_or_approval'] = await run_obtain_fda_clearance_or_approval()

    # Return all results
    return results

def run_workflow_sync(user_input: str) -> Dict[str, Any]:
    """Synchronous wrapper around the async workflow execution."""
    return asyncio.run(run_workflow(user_input))

def main():
    """Main entry point.

    Handles arguments in the following priority:
    1. Command-line argument (sys.argv[1])
    2. If no argument, uses empty string as input but displays a warning.
    """
    # Get user input from command line or use empty string
    if len(sys.argv) > 1:
        user_input = sys.argv[1]
    else:
        # No input provided - display help message but continue with empty string
        print('Warning: No input provided. Using empty string as input.')
        print('For better results, provide an input argument:')
        print(f'  python {os.path.basename(__file__)} "your input text here"')
        print('Or use a file as input:')
        print(f'  python {os.path.basename(__file__)} "$(cat input.txt)"')
        user_input = ""

    print(f'Running workflow with input: {user_input}')

    # Run the workflow
    results = run_workflow_sync(user_input)

    # Print results
    try:
        # Convert results to JSON
        json_results = json.dumps(results, indent=2, default=str)
        print(json_results)
    except (TypeError, ValueError) as e:
        print(f'Results could not be converted to JSON: {e}')
        print(f'Raw results: {results}')

    return results

if __name__ == '__main__':
    main()
