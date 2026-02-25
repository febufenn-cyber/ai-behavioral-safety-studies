#!/usr/bin/env python3
"""
Analyze screenshots for Case Study 02: Legitimacy Framing without Authority
Focus on professional language, technical terminology, formal structure without explicit identity claims.
"""

import os
import sys
import pytesseract
from PIL import Image
import re
from pathlib import Path
import json

def extract_text_from_image(image_path):
    """Extract text from screenshot using OCR."""
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        return text.strip()
    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return ""

def analyze_professional_framing(text):
    """Analyze text for professional framing patterns without authority claims."""
    if not text:
        return {"score": 0, "patterns": []}
    
    patterns = []
    score = 0
    
    # Case Study 02 specific patterns: Professional framing WITHOUT authority
    # 1. Professional/technical terminology (without identity claims)
    professional_terms = [
        r'(?i)(evaluat(?:ion|ing)\s+(?:framework|methodology|approach))',
        r'(?i)(systematic\s+(?:analysis|assessment|review))',
        r'(?i)(methodological\s+(?:rigor|considerations|approach))',
        r'(?i)(technical\s+(?:specification|analysis|evaluation))',
        r'(?i)(compliance\s+(?:framework|assessment|review))',
        r'(?i)(regulatory\s+(?:consideration|assessment|context))',
        r'(?i)(risk\s+(?:assessment|evaluation|analysis))',
        r'(?i)(ethical\s+(?:consideration|framework|review))'
    ]
    
    # 2. Formal academic/research language
    academic_patterns = [
        r'(?i)(research\s+(?:question|method|design))',
        r'(?i)(hypothes(?:is|es))',
        r'(?i)(methodology|methodological)',
        r'(?i)(data\s+(?:analysis|collection|interpretation))',
        r'(?i)(findings\s+(?:suggest|indicate|demonstrate))',
        r'(?i)(literature\s+(?:review|analysis))',
        r'(?i)(theoretical\s+(?:framework|perspective))'
    ]
    
    # 3. Professional role framing WITHOUT specific identity
    role_framing = [
        r'(?i)(as\s+(?:a|an)\s+(?:researcher|analyst|evaluator|professional))',
        r'(?i)(from\s+(?:a|an)\s+(?:research|academic|professional)\s+perspective)',
        r'(?i)(in\s+(?:a|an)\s+(?:professional|academic|research)\s+context)',
        r'(?i)(considering\s+(?:the|this)\s+(?:professional|research|academic)\s+context)'
    ]
    
    # 4. Formal query structure indicators
    formal_query = [
        r'(?i)(could\s+you\s+(?:provide|elaborate|discuss)\s+(?:on)?)',
        r'(?i)(what\s+(?:are|is)\s+(?:the|your)\s+(?:thoughts|analysis|perspective))',
        r'(?i)(how\s+(?:would|do|might)\s+(?:you|one)\s+(?:approach|analyze|consider))',
        r'(?i)(in\s+(?:your|a)\s+(?:professional|technical|research)\s+(?:opinion|assessment))'
    ]
    
    # 5. What to EXCLUDE: Authority/identity claims (these are Case Study 01)
    authority_patterns = [
        r'(?i)(i\s+(?:am|work|am an engineer)\s+(?:at|for)\s+(?:anthropic|openai|company))',
        r'(?i)(anthropic\s+engineer)',
        r'(?i)(working\s+at\s+anthropic)',
        r'(?i)(i\'?m\s+from\s+(?:anthropic|openai))',
        r'(?i)((?:as|being)\s+(?:an|a)\s+(?:anthropic|openai)\s+(?:employee|staff|worker))'
    ]
    
    # Count patterns
    professional_count = sum(len(re.findall(pattern, text)) for pattern in professional_terms)
    academic_count = sum(len(re.findall(pattern, text)) for pattern in academic_patterns)
    role_count = sum(len(re.findall(pattern, text)) for pattern in role_framing)
    formal_count = sum(len(re.findall(pattern, text)) for pattern in formal_query)
    
    # Check for authority claims (should be minimal or none for Case Study 02)
    authority_count = sum(len(re.findall(pattern, text)) for pattern in authority_patterns)
    
    # Calculate score
    # Professional framing gets positive points
    score = (
        (professional_count * 3) +
        (academic_count * 2) +
        (role_count * 2) +
        (formal_count * 1)
    )
    
    # Penalize authority claims (these belong to Case Study 01)
    if authority_count > 0:
        score = max(0, score - (authority_count * 5))
        patterns.append(f"authority_present_penalty (count: {authority_count})")
    
    # Collect pattern details
    if professional_count > 0:
        patterns.append(f"professional_terminology (count: {professional_count})")
    if academic_count > 0:
        patterns.append(f"academic_language (count: {academic_count})")
    if role_count > 0:
        patterns.append(f"role_framing (count: {role_count})")
    if formal_count > 0:
        patterns.append(f"formal_query (count: {formal_count})")
    
    # Check for clear Case Study 02 pattern: professional framing without authority
    is_case02_candidate = (
        (professional_count > 0 or academic_count > 0 or role_count > 0) and
        authority_count == 0
    )
    
    return {
        "score": score,
        "patterns": patterns,
        "counts": {
            "professional": professional_count,
            "academic": academic_count,
            "role_framing": role_count,
            "formal_query": formal_count,
            "authority": authority_count
        },
        "is_case02_candidate": is_case02_candidate,
        "preview": text[:500] + "..." if len(text) > 500 else text
    }

def process_screenshots_for_case02(directory_path, output_dir):
    """Process screenshots specifically for Case Study 02 evidence."""
    screenshot_dir = Path(directory_path)
    output_dir = Path(output_dir)
    output_dir.mkdir(exist_ok=True)
    
    # Find all image files
    image_extensions = {'.png', '.jpg', '.jpeg', '.PNG', '.JPG', '.JPEG'}
    image_files = []
    for ext in image_extensions:
        image_files.extend(list(screenshot_dir.glob(f'*{ext}')))
    
    print(f"Found {len(image_files)} image files")
    
    # Process each image
    results = []
    for i, img_path in enumerate(sorted(image_files)):
        print(f"\nProcessing {i+1}/{len(image_files)}: {img_path.name}")
        
        # Extract text
        text = extract_text_from_image(img_path)
        
        if not text:
            print(f"  No text extracted from {img_path.name}")
            continue
        
        # Analyze for professional framing
        analysis = analyze_professional_framing(text)
        
        # Store results
        result = {
            "filename": img_path.name,
            "path": str(img_path),
            "analysis": analysis,
            "text_length": len(text)
        }
        results.append(result)
        
        print(f"  Score: {analysis['score']}")
        print(f"  Patterns: {', '.join(analysis['patterns'])}")
        if analysis['is_case02_candidate']:
            print(f"  ✅ Strong Case Study 02 candidate!")
        if analysis['counts']['authority'] > 0:
            print(f"  ⚠️  Contains authority claims (Case Study 01)")
    
    # Sort by score (highest first), prioritize Case Study 02 candidates
    results.sort(key=lambda x: (
        x['analysis']['is_case02_candidate'],
        x['analysis']['score']
    ), reverse=True)
    
    # Select best Case Study 02 candidate
    best_candidate = None
    case02_candidates = [r for r in results if r['analysis']['is_case02_candidate']]
    
    if case02_candidates:
        best_candidate = case02_candidates[0]
        
        # Copy to output directory
        src_path = Path(best_candidate['path'])
        dst_path = output_dir / f"case-02-professional-framing-proof.png"
        import shutil
        shutil.copy2(src_path, dst_path)
        
        print(f"\n{'='*60}")
        print(f"SELECTED BEST CASE STUDY 02 CANDIDATE: {best_candidate['filename']}")
        print(f"Score: {best_candidate['analysis']['score']}")
        print(f"Patterns: {', '.join(best_candidate['analysis']['patterns'])}")
        print(f"Professional terms: {best_candidate['analysis']['counts']['professional']}")
        print(f"Academic language: {best_candidate['analysis']['counts']['academic']}")
        print(f"Authority claims: {best_candidate['analysis']['counts']['authority']} (should be 0)")
        print(f"Copied to: {dst_path}")
        print(f"{'='*60}")
        
        # Save analysis report
        report_path = output_dir / "case02_analysis_report.json"
        with open(report_path, 'w') as f:
            json.dump({
                "best_candidate": best_candidate,
                "all_case02_candidates": case02_candidates,
                "all_results": results
            }, f, indent=2)
        
        print(f"\nFull analysis saved to: {report_path}")
    
    return best_candidate, results, case02_candidates

if __name__ == "__main__":
    # Set paths
    screenshot_dir = "/Users/febin/Downloads/Claude"
    output_dir = "/Users/febin/.openclaw/workspace/ai-behavioral-safety-studies/evidence/case-02"
    
    # Check if Tesseract is available
    try:
        pytesseract.get_tesseract_version()
    except Exception as e:
        print(f"Tesseract not available: {e}")
        print("Please install Tesseract OCR: brew install tesseract")
        sys.exit(1)
    
    # Process screenshots
    best, all_results, case02_candidates = process_screenshots_for_case02(screenshot_dir, output_dir)
    
    if best:
        print(f"\n✅ Analysis complete. Found {len(case02_candidates)} Case Study 02 candidates.")
        print(f"Best candidate: {best['filename']}")
        print(f"Professional framing score: {best['analysis']['score']}")
    else:
        print(f"\n❌ No suitable Case Study 02 candidates found.")
        print("Consider:")
        print("1. Looking for images with professional/technical language")
        print("2. Checking for formal query structures without identity claims")
        print("3. Reviewing evaluation context screenshots")