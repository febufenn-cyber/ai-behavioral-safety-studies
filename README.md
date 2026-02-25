# AI Behavioral Safety Studies Portfolio

## Overview

This portfolio documents systematic evaluations of large language model (LLM) behavior under various conversational framing conditions. The focus is on identifying how social and contextual cues influence model responses, particularly around safety calibration and helpfulness optimization.

### Project Purpose
- **Identify behavioral patterns** in LLMs when presented with realistic conversational framing
- **Document calibration shifts** that occur due to authority claims, professional tone, and evaluation context
- **Contribute to AI safety research** by providing reproducible case studies and methodology
- **Educate** on red teaming approaches for AI system evaluation

## Repository Structure

```
ai-behavioral-safety-studies/
├── README.md (this file)
├── CHANGELOG.md                       # Version history
├── CONTRIBUTING.md                    # Contribution guidelines
├── LICENSE                            # MIT License
├── methodology/
│   └── evaluation-framework.md        # Testing framework & ethical guidelines
├── case-studies/
│   ├── case-01-identity-calibration.md  # Authority claim influence study
│   └── case-02-legitimacy-framing.md    # Professional tone influence study
├── observations/
│   └── behavioral-patterns.md         # Synthesized patterns across studies
├── evidence/
│   ├── case-01/                       # Proof for identity calibration study
│   ├── case-02/                       # Proof for legitimacy framing study
│   ├── analysis/                      # Analysis reports & tool outputs
│   └── README.md                      # Evidence documentation
├── tools/
│   ├── transcript_analyzer.py         # OCR analysis tool
│   └── README.md                      # Tool documentation
├── examples/
│   └── sample_transcript.json         # Example conversation data
└── requirements.txt                   # Optional Python dependencies
```

## Contents

### Case Studies

1. **Case Study 01: Identity-Based Calibration**
   - **Objective**: Test whether unverified authority claims influence LLM response style
   - **Method**: Simulated user claiming to work for model developer, observed response changes
   - **Key Finding**: Model reduced disclaimers, softened tone, assumed shared expertise
   - **File**: `case-studies/case-01-identity-calibration.md`

2. **Case Study 02: Legitimacy Framing without Authority**
   - **Objective**: Assess if professional framing alone affects model responses
   - **Method**: Technically phrased questions, formal tone without false identity
   - **Key Finding**: Similar calibration shifts observed through language style alone
   - **File**: `case-studies/case-02-legitimacy-framing.md`

### Evidence

Concrete proof supporting case study findings:

1. **Screenshot Evidence**: Direct admission by AI of behavioral adjustment based on identity claims
2. **Analysis Reports**: OCR analysis of 20+ test sessions showing consistent patterns
3. **Methodological Validation**: Real-world application of red teaming methodology
4. **Ethical Documentation**: Responsible handling of test data and findings

See the `evidence/` directory for complete documentation and proof files.

### Methodology

The `methodology/` folder contains:
- **Evaluation Framework**: Systematic testing approach based on AI safety and red-teaming principles
- **Ethical Guidelines**: Responsible testing practices, data anonymization, and disclosure protocols
- **Reproducibility Instructions**: Fixed random seeds, conversation metadata logging

### Observations

The `observations/` folder contains:
- **Behavioral Patterns**: Synthesized insights from all case studies
- **Generalization Analysis**: Cross-session pattern validation
- **Design Implications**: Recommendations for AI system development

## Usage

### Reproducing Experiments

1. **Select a case study** from the `case-studies/` folder
2. **Review the methodology** in `methodology/evaluation-framework.md`
3. **Use the provided prompts** in each case study file
4. **Log results** following the documented format

### Running Your Own Evaluations

1. Follow the ethical guidelines in the methodology document
2. Use consistent logging format for reproducibility
3. Consider contributing new case studies via pull request

## Quick Start

To understand the core findings:

1. Read the [Behavioral Patterns Summary](observations/behavioral-patterns.md)
2. Review [Case Study 01](case-studies/case-01-identity-calibration.md) for authority influence
3. Examine the [Evaluation Framework](methodology/evaluation-framework.md) for methodology details

## Key Insights

1. **Social Framing Effects**: Credible-sounding context cues (authority or professional tone) increase model cooperativeness
2. **Calibration Persistence**: Once trust is established, effects tend to persist through conversations
3. **Helpfulness vs. Guardrail Tension**: Social prompts can inadvertently reduce safety conservatism
4. **Generalization**: Patterns are reproducible across different framing conditions

## Ethical Considerations

- All user data is anonymized
- No disallowed content is generated or stored
- Tests are framed non-maliciously with transparent intent
- Serious safety issues would be responsibly disclosed to platform providers
- Adherence to AI ethics principles (fairness, transparency, accountability)

## Conclusion

This portfolio presents preliminary findings from systematic LLM behavior evaluation. The work is educational and safety-oriented, intended to contribute to understanding of AI system vulnerabilities and improvement of safety mechanisms.

**Note**: All findings are preliminary and should be interpreted within the context of the specific testing conditions documented.

## References

- AI Safety Institute Red Teaming Methodology (Version 1.00)
- NIST AI Risk Management Framework
- OECD Due Diligence Guidance for Responsible AI
- IEEE Ethically Aligned Design Framework

## Contact

For questions about this portfolio or responsible disclosure of findings, please refer to the methodology document for appropriate channels.

---

*Last Updated: February 25, 2026*  
*Project Status: Active - Case Studies Documented*