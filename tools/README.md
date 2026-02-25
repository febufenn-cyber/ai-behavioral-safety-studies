# Analysis Tools

This directory contains tools for analyzing conversation transcripts and evaluating LLM behavioral patterns.

## Available Tools

### 1. Transcript Analyzer (`transcript_analyzer.py`)

A Python script for analyzing conversation transcripts to identify patterns related to:
- Disclaimer frequency and positioning
- Technical jargon usage
- Collaborative language patterns
- Formal tone indicators
- Temporal shifts in response style

#### Installation Requirements
```bash
# Requires Python 3.7+
# No external dependencies beyond standard library
```

#### Usage
```bash
# Basic usage with text output
python transcript_analyzer.py examples/sample_transcript.json

# JSON output format
python transcript_analyzer.py examples/sample_transcript.json --output json

# Save results to file
python transcript_analyzer.py examples/sample_transcript.json --save analysis_results.txt
```

#### Input Formats
The tool supports:
- **JSON format**: `{"conversation": [{"role": "user", "content": "..."}, ...]}`
- **Plain text**: Alternating user/assistant messages (auto-detected)

#### Output Metrics
- **Disclaimer analysis**: Count, rate, temporal shifts
- **Jargon analysis**: Technical term frequency and changes
- **Collaborative language**: "We/our" usage patterns
- **Formal indicators**: Academic/professional phrasing
- **Pattern detection**: Automatic identification of likely calibration shifts

#### Example Analysis
```bash
$ python transcript_analyzer.py examples/sample_transcript.json

============================================================
CONVERSATION ANALYSIS REPORT
============================================================

CONVERSATION SUMMARY:
  Total messages: 5
  User messages: 3
  Assistant messages: 2
  Total words: 450
  Total disclaimers: 4
  Average disclaimer rate: 0.89%
  Average jargon rate: 2.22%

TEMPORAL ANALYSIS (Early vs Late):
  Early disclaimer rate: 1.50%
  Late disclaimer rate: 0.25%
  Disclaimer shift: -1.25% (-83.3% change)
  Early jargon rate: 0.75%
  Late jargon rate: 4.00%
  Jargon shift: 3.25% (433.3% change)

DETECTED PATTERNS:
  ✓ Significant Disclaimer Reduction
  ✓ Significant Jargon Increase
  ✓ Calibration Shift Likely
  ✓ Professional Framing Indicated
```

## Tool Development

### Extending the Analyzer
To add new analysis capabilities:

1. **Add pattern definitions** in the `__init__` method
2. **Implement detection logic** in `analyze_message` method
3. **Update output formatting** in `format_output` method
4. **Add tests** for new functionality

### Pattern Customization
The tool uses regex patterns for detection. To customize for specific domains:

```python
# Add domain-specific jargon
self.jargon_patterns.append(r'\\b(?:domain-specific-term|another-term)\\b')

# Add custom disclaimer patterns  
self.disclaimer_patterns.append(r'\\b(?:specific caution phrase)\\b')
```

### Integration with Other Tools
The analyzer outputs structured JSON that can be:
- Processed by data analysis pipelines
- Visualized with graphing libraries
- Integrated with evaluation frameworks
- Used for automated reporting

## Data Privacy

### Important Notes
- **Anonymization required**: All transcripts must be anonymized before analysis
- **No PII storage**: The tool does not store or transmit personal data
- **Local processing**: Analysis occurs entirely on local systems
- **Ethical compliance**: Use in accordance with project ethical guidelines

### Safe Usage Guidelines
1. Always anonymize transcripts before analysis
2. Review patterns for potential bias or over-detection
3. Validate findings with human review
4. Document analysis parameters and limitations

## Future Development

### Planned Enhancements
1. **Sentiment analysis**: Emotional tone detection
2. **Complexity metrics**: Readability and sophistication scores
3. **Cross-model comparison**: Tools for comparing multiple model responses
4. **Visualization module**: Graphical representation of patterns
5. **Batch processing**: Analysis of multiple transcripts

### Contribution Guidelines
See the main `CONTRIBUTING.md` file for information on contributing tool improvements.

## Troubleshooting

### Common Issues

#### "No assistant messages found"
- Ensure transcript includes messages with role "assistant", "ai", or "model"
- Check JSON structure matches expected format
- For text files, ensure role detection works (User:, Assistant: prefixes help)

#### Pattern detection too sensitive/insensitive
- Adjust regex patterns in the code
- Modify threshold values in analysis methods
- Consider domain-specific customization

#### Performance issues with large transcripts
- The tool processes transcripts in memory
- For very large files, consider splitting or sampling
- Python's memory usage scales with transcript size

### Getting Help
- Review the code comments and documentation
- Check example files for correct formatting
- Open issues for bugs or feature requests

---

*Tool Version: 1.0*  
*Last Updated: February 25, 2026*