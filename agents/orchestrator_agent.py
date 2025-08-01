import json
import os
from agents.classifier_agent import classify_email
from agents.response_generator_agent import generate_response
from agents.quality_checker_agent import check_response_quality

def run_workflow(email_text, report_folder="reports"):
    
    # email classifier
    classification = classify_email(email_text)
    print("\n[Classifier Agent Output]:\n", classification)

    # error check
    if "[ERROR]" in classification or ":" not in classification:
        print("\n[Orchestrator]: Classification failed. Skipping response generation.")
        return

    try:
        # clean,parse logical lines
        lines = [line for line in classification.strip().splitlines() if ":" in line]
        category = lines[0].split(":")[1].strip()
        sender_name = lines[1].split(":")[1].strip()
        company_name = lines[2].split(":")[1].strip()
        needs_response = lines[3].split(":")[1].strip()
    except Exception as e:
        print(f"\n[Orchestrator]: Failed to parse classification output: {e}")
        return

    # category normalization
    category_clean = category.strip().lower()

    # escalating verification
    if category_clean == "verification":
        print("\n[Orchestrator]: escalated to human — verification email.")
        return

    if category_clean not in ["support", "newsletter", "outbound"]:
        print("\n[Orchestrator]: escalated to human — unknown category.")
        return

    # generating response when needed
    if needs_response.lower() == "yes":
        response = generate_response(email_text, sender_name, company_name, category_clean)
        print("\n[response generator output]:\n", response)

        # checking the quality of response
        quality_report = check_response_quality(response)
        print("\n[quality checker output]:\n", quality_report)

        # saving result
        if not os.path.exists(report_folder):
            os.makedirs(report_folder)

        report_data = {
            "sender": sender_name,
            "company": company_name,
            "category": category_clean,
            "response": response,
            "quality_report": quality_report
        }

        filename = f"{report_folder}/{sender_name.lower().replace(' ', '_')}_report.json"
        with open(filename, "w") as f:
            json.dump(report_data, f, indent=4)

        print(f"\n[saved]: {filename}")
    else:
        print("\n[orchestrator]: no response needed.")