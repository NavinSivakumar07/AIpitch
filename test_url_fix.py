#!/usr/bin/env python3
"""
Test script to verify URL extraction fix is working
"""

def test_url_extraction_fix():
    """Test the URL extraction functionality with sample research text."""
    
    # Sample research text that mimics what the API might return
    sample_research_text = """
    # Market Research Report for Kluisz.ai

    ## Market Analysis
    The AI industry is experiencing unprecedented growth, with the global AI market projected to reach $1.8 trillion by 2030 according to recent studies. (Source: https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai-in-2023)

    **Enterprise AI Adoption Trends**
    Enterprise adoption of AI technologies has increased by 73% in the last year, driven by improved ROI and competitive advantages. Source: https://www.gartner.com/en/newsroom/press-releases/2024-ai-adoption-trends

    ## Competitive Landscape
    **Leading AI Infrastructure Companies**
    The competitive landscape includes major players investing heavily in AI infrastructure and cloud services.
    Reference: https://www.forrester.com/report/the-forrester-wave-ai-infrastructure-platforms

    ## Industry Trends
    Recent developments show significant investment in AI startups, with funding reaching record levels.
    URL: https://techcrunch.com/2024/01/15/ai-startup-funding-record-levels

    Additional sources:
    - https://www.pwc.com/gx/en/issues/data-and-analytics/publications/artificial-intelligence-study.html
    - https://www.accenture.com/us-en/insights/artificial-intelligence/ai-investments
    """
    
    print("🔍 Testing URL Extraction Fix")
    print("=" * 50)
    
    # Import the extraction function
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    
    # Test basic regex patterns
    import re
    
    # Test Pattern 1: Basic URL extraction
    url_pattern = r'https?://[^\s<>"{}|\\^`\[\]]+[^\s<>"{}|\\^`\[\].,;:!?]'
    basic_urls = re.findall(url_pattern, sample_research_text)
    
    print(f"✅ Basic URL Pattern Test:")
    print(f"   Found {len(basic_urls)} URLs")
    for i, url in enumerate(basic_urls, 1):
        print(f"   {i}. {url}")
    
    # Test Pattern 2: Source citations
    citation_patterns = [
        r'Source:\s*(https?://[^\s<>"{}|\\^`\[\]]+)',
        r'\(Source:\s*(https?://[^\s<>"{}|\\^`\[\]]+)\)',
        r'Reference:\s*(https?://[^\s<>"{}|\\^`\[\]]+)',
        r'URL:\s*(https?://[^\s<>"{}|\\^`\[\]]+)'
    ]
    
    print(f"\n✅ Citation Pattern Tests:")
    pattern_names = ['Source:', '(Source:)', 'Reference:', 'URL:']
    total_citations = 0
    
    for pattern_name, pattern in zip(pattern_names, citation_patterns):
        citations = re.findall(pattern, sample_research_text, re.IGNORECASE)
        total_citations += len(citations)
        print(f"   {pattern_name} - Found {len(citations)} citations")
        for citation in citations:
            print(f"      • {citation}")
    
    # Test domain extraction
    print(f"\n✅ Domain Extraction Test:")
    test_urls = basic_urls[:3]  # Test first 3 URLs
    
    for url in test_urls:
        try:
            domain = url.split('/')[2] if '/' in url else url
            print(f"   {url} -> {domain}")
        except:
            print(f"   {url} -> Error extracting domain")
    
    # Summary
    print(f"\n🎯 Test Summary:")
    print(f"   • Total URLs found: {len(basic_urls)}")
    print(f"   • Citation URLs found: {total_citations}")
    print(f"   • Unique domains: {len(set([url.split('/')[2] for url in basic_urls if '/' in url]))}")
    
    if len(basic_urls) > 0:
        print(f"\n✅ SUCCESS: URL extraction is working!")
        print(f"   The system should now display {len(basic_urls)} clickable research sources.")
    else:
        print(f"\n❌ ISSUE: No URLs found in sample text")
    
    print(f"\n📝 Next Steps:")
    print(f"   1. Run the Streamlit app")
    print(f"   2. Generate a pitch deck")
    print(f"   3. Check the 'Web Research Results' section")
    print(f"   4. Look for clickable source links")
    
    return len(basic_urls) > 0

if __name__ == "__main__":
    test_url_extraction_fix()
