#!/bin/bash

# AI Behavioral Safety Studies Portfolio Demo Script
# Demonstrates the portfolio structure and tools

echo "================================================"
echo "AI Behavioral Safety Studies Portfolio Demo"
echo "================================================"
echo ""

# Check Python availability
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
elif command -v python &> /dev/null; then
    PYTHON_CMD="python"
else
    echo "ERROR: Python not found. Please install Python 3.7 or higher."
    exit 1
fi

echo "1. Validating portfolio structure..."
$PYTHON_CMD validate_portfolio.py

echo ""
echo "2. Displaying portfolio structure..."
find . -type f -name "*.md" -o -name "*.py" -o -name "*.json" -o -name "*.txt" | sort | grep -v "__pycache__" | head -20

echo ""
echo "3. Analyzing sample transcript with transcript analyzer..."
if [ -f "examples/sample_transcript.json" ]; then
    echo "Running transcript analysis..."
    $PYTHON_CMD tools/transcript_analyzer.py examples/sample_transcript.json --output text
else
    echo "ERROR: Sample transcript not found at examples/sample_transcript.json"
fi

echo ""
echo "4. Key files summary:"
echo "   - README.md: $(wc -l < README.md) lines"
echo "   - Methodology: $(wc -l < methodology/evaluation-framework.md) lines"
echo "   - Case Study 01: $(wc -l < case-studies/case-01-identity-calibration.md) lines"
echo "   - Case Study 02: $(wc -l < case-studies/case-02-legitimacy-framing.md) lines"
echo "   - Observations: $(wc -l < observations/behavioral-patterns.md) lines"

echo ""
echo "5. Portfolio overview:"
echo "   This portfolio contains:"
echo "   - 2 detailed case studies on LLM behavioral patterns"
echo "   - Comprehensive evaluation methodology and ethical guidelines"
echo "   - Synthesized observations across studies"
echo "   - Analysis tools for transcript evaluation"
echo "   - Example data and documentation"
echo ""
echo "   The portfolio demonstrates systematic evaluation of:"
echo "   - Identity-based calibration shifts in LLMs"
echo "   - Legitimacy framing effects through language style"
echo "   - Social engineering vulnerabilities"
echo "   - Helpfulness vs. safety guardrail tensions"

echo ""
echo "6. Next steps:"
echo "   - Read README.md for full documentation"
echo "   - Review case studies in case-studies/ directory"
echo "   - Examine methodology/evaluation-framework.md for testing approach"
echo "   - Use tools/transcript_analyzer.py to analyze your own transcripts"
echo "   - See CONTRIBUTING.md for contribution guidelines"

echo ""
echo "================================================"
echo "Demo complete. Portfolio is ready for use."
echo "================================================"