#!/usr/bin/env python3
"""
Portfolio Validation Script

Validates the structure and content of the AI Behavioral Safety Studies portfolio.
Checks for required files, directory structure, and basic content validity.
"""

import os
import sys
import json
from pathlib import Path
from typing import Dict, List, Tuple

class PortfolioValidator:
    """Validate portfolio structure and content."""
    
    REQUIRED_FILES = [
        "README.md",
        "LICENSE",
        "CONTRIBUTING.md",
        ".gitignore",
        "methodology/evaluation-framework.md",
        "case-studies/case-01-identity-calibration.md",
        "case-studies/case-02-legitimacy-framing.md",
        "observations/behavioral-patterns.md",
        "tools/transcript_analyzer.py",
        "tools/README.md",
        "examples/sample_transcript.json"
    ]
    
    REQUIRED_DIRECTORIES = [
        "methodology",
        "case-studies",
        "observations",
        "tools",
        "examples"
    ]
    
    MIN_FILE_SIZES = {
        "README.md": 1000,
        "methodology/evaluation-framework.md": 2000,
        "case-studies/case-01-identity-calibration.md": 3000,
        "case-studies/case-02-legitimacy-framing.md": 3000,
        "observations/behavioral-patterns.md": 2000
    }
    
    REQUIRED_SECTIONS = {
        "README.md": ["Overview", "Repository Structure", "Contents", "Usage"],
        "methodology/evaluation-framework.md": ["Testing Philosophy", "Methodology", "Ethical Guidelines"],
        "case-studies/case-01-identity-calibration.md": ["Executive Summary", "Study Design", "Results", "Analysis"],
        "case-studies/case-02-legitimacy-framing.md": ["Executive Summary", "Study Design", "Results", "Analysis"],
        "observations/behavioral-patterns.md": ["Key Patterns Identified", "Safety Implications"]
    }
    
    def __init__(self, portfolio_path: str):
        self.portfolio_path = Path(portfolio_path)
        self.errors = []
        self.warnings = []
        self.successes = []
    
    def validate_structure(self):
        """Validate directory and file structure."""
        self.successes.append("Starting portfolio validation...")
        
        # Check portfolio directory exists
        if not self.portfolio_path.exists():
            self.errors.append(f"Portfolio directory not found: {self.portfolio_path}")
            return
        
        # Check required directories
        for dir_path in self.REQUIRED_DIRECTORIES:
            full_path = self.portfolio_path / dir_path
            if not full_path.exists():
                self.errors.append(f"Missing required directory: {dir_path}")
            elif not full_path.is_dir():
                self.errors.append(f"Not a directory (should be): {dir_path}")
            else:
                self.successes.append(f"✓ Directory exists: {dir_path}")
        
        # Check required files
        for file_path in self.REQUIRED_FILES:
            full_path = self.portfolio_path / file_path
            if not full_path.exists():
                self.errors.append(f"Missing required file: {file_path}")
            elif not full_path.is_file():
                self.errors.append(f"Not a file (should be): {file_path}")
            else:
                self.successes.append(f"✓ File exists: {file_path}")
                
                # Check file size for key documents
                if file_path in self.MIN_FILE_SIZES:
                    file_size = full_path.stat().st_size
                    min_size = self.MIN_FILE_SIZES[file_path]
                    if file_size < min_size:
                        self.warnings.append(f"File may be too small: {file_path} ({file_size} < {min_size} bytes)")
                    else:
                        self.successes.append(f"  File size adequate: {file_size} bytes")
    
    def validate_content(self):
        """Validate content of key files."""
        for file_path, required_sections in self.REQUIRED_SECTIONS.items():
            full_path = self.portfolio_path / file_path
            if full_path.exists():
                try:
                    with open(full_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    missing_sections = []
                    for section in required_sections:
                        # Look for section headers (markdown format)
                        if f"# {section}" not in content and f"## {section}" not in content:
                            # Try with different formatting
                            if section.lower() not in content.lower():
                                missing_sections.append(section)
                    
                    if missing_sections:
                        self.warnings.append(f"File {file_path} may be missing sections: {', '.join(missing_sections)}")
                    else:
                        self.successes.append(f"✓ File {file_path} contains required sections")
                        
                except Exception as e:
                    self.errors.append(f"Error reading {file_path}: {e}")
    
    def validate_examples(self):
        """Validate example files."""
        example_path = self.portfolio_path / "examples" / "sample_transcript.json"
        if example_path.exists():
            try:
                with open(example_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                
                # Check basic structure
                if "conversation" not in data:
                    self.errors.append("Sample transcript missing 'conversation' key")
                elif not isinstance(data["conversation"], list):
                    self.errors.append("Sample transcript 'conversation' should be a list")
                else:
                    self.successes.append("✓ Sample transcript JSON structure valid")
                    
                    # Check for expected patterns
                    content = json.dumps(data)
                    if "Anthropic" in content and "disclaimer" in content.lower():
                        self.successes.append("✓ Sample transcript contains expected patterns")
                    else:
                        self.warnings.append("Sample transcript may not demonstrate expected patterns")
                        
            except json.JSONDecodeError as e:
                self.errors.append(f"Invalid JSON in sample transcript: {e}")
            except Exception as e:
                self.errors.append(f"Error validating example: {e}")
    
    def validate_tools(self):
        """Validate tool files."""
        tool_path = self.portfolio_path / "tools" / "transcript_analyzer.py"
        if tool_path.exists():
            try:
                with open(tool_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Check for key components
                checks = [
                    ("class TranscriptAnalyzer", "TranscriptAnalyzer class"),
                    ("def analyze_message", "analyze_message method"),
                    ("def analyze_conversation", "analyze_conversation method"),
                    ("def main", "main function"),
                    ("argparse", "argument parsing"),
                    ("disclaimer_patterns", "disclaimer patterns")
                ]
                
                for pattern, description in checks:
                    if pattern in content:
                        self.successes.append(f"✓ Tool contains {description}")
                    else:
                        self.warnings.append(f"Tool may be missing {description}")
                        
            except Exception as e:
                self.errors.append(f"Error validating tools: {e}")
    
    def run_validation(self) -> bool:
        """Run all validation checks."""
        self.validate_structure()
        self.validate_content()
        self.validate_examples()
        self.validate_tools()
        
        # Summary
        print("\n" + "="*60)
        print("PORTFOLIO VALIDATION RESULTS")
        print("="*60)
        
        if self.successes:
            print(f"\nSUCCESSES ({len(self.successes)}):")
            for success in self.successes[:10]:  # Limit output
                print(f"  {success}")
            if len(self.successes) > 10:
                print(f"  ... and {len(self.successes) - 10} more")
        
        if self.warnings:
            print(f"\nWARNINGS ({len(self.warnings)}):")
            for warning in self.warnings:
                print(f"  ⚠ {warning}")
        
        if self.errors:
            print(f"\nERRORS ({len(self.errors)}):")
            for error in self.errors:
                print(f"  ✗ {error}")
        
        print("\n" + "="*60)
        
        if self.errors:
            print(f"VALIDATION FAILED: {len(self.errors)} errors found")
            return False
        elif self.warnings:
            print(f"VALIDATION PASSED with {len(self.warnings)} warnings")
            return True
        else:
            print(f"VALIDATION PASSED: Portfolio structure and content are valid")
            return True

def main():
    """Main validation function."""
    # Default to current directory if not specified
    if len(sys.argv) > 1:
        portfolio_path = sys.argv[1]
    else:
        # Assume script is run from portfolio root
        portfolio_path = "."
    
    validator = PortfolioValidator(portfolio_path)
    success = validator.run_validation()
    
    # Exit with appropriate code
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()