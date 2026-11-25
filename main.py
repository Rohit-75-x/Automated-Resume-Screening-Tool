"""CLI entry point for Automated Resume Screening Tool."""

import argparse
from pathlib import Path
import sys

from src.config import DATA_DIR, RESUMES_DIR
from src.pipeline import load_job_description, load_resumes_from_directory, run_screening_pipeline
from src.sample_generator import generate_sample_dataset


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Automated Resume Screening Tool CLI")
    parser.add_argument(
        "--resumes-dir",
        type=Path,
        default=RESUMES_DIR,
        help="Directory containing candidate resumes (.pdf, .docx, .txt, .md).",
    )
    parser.add_argument(
        "--jd-file",
        type=Path,
        default=DATA_DIR / "job_description.json",
        help="Path to the target job description JSON file.",
    )
    parser.add_argument(
        "--seed-samples",
        action="store_true",
        help="Generate synthetic PDF/DOCX/TXT resumes and sample job description before running.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.seed_samples or not args.jd_file.exists() or not any(args.resumes_dir.glob("*")):
        generate_sample_dataset(overwrite=args.seed_samples)

    job = load_job_description(args.jd_file)
    resumes = load_resumes_from_directory(args.resumes_dir)
    if not resumes:
        print(f"No supported resumes found in {args.resumes_dir}")
        return 1

    result = run_screening_pipeline(resumes, job, save_outputs=True)

    print("\n" + "=" * 78)
    print("  AUTOMATED RESUME SCREENING TOOL — RANKING REPORT")
    print("=" * 78)
    print(f"Job Title       : {result.summary.job_title}")
    print(f"Total Resumes   : {result.summary.total_candidates}")
    print(
        f"Decisions       : Shortlisted={result.summary.shortlisted_count} | "
        f"Borderline={result.summary.borderline_count} | "
        f"Rejected={result.summary.rejected_count}"
    )
    print(f"Average Score   : {result.summary.average_score}/100")
    print(f"CSV Report      : {result.csv_report_path}")
    if result.chart_path:
        print(f"Ranking Chart   : {result.chart_path}")
    print("-" * 78)
    for cand in result.candidates:
        gaps = ", ".join(cand.missing_must_have) if cand.missing_must_have else "None"
        print(
            f"#{cand.rank} | {cand.candidate_name:18s} | {cand.final_score:5.1f}/100 | "
            f"{cand.decision:11s} | Exp: {cand.years_experience:4.1f}y | Gaps: {gaps}"
        )
        print(f"     -> {cand.explanation}")
    print("=" * 78 + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
