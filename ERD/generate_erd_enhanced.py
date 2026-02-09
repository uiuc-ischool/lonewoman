#!/usr/bin/env python3
"""
Enhanced ERD Generator for Lone Woman Historical Newspaper Collection
Uses traditional crow's foot notation and improved layout
"""

import pandas as pd
from graphviz import Digraph
import sys

def create_enhanced_erd(csv_file, output_file='lonewoman_erd_enhanced'):
    """
    Create an enhanced ERD with better layout and crow's foot notation
    """
    
    # Read the CSV
    df = pd.read_csv(csv_file)
    
    # Create a new directed graph for ERD
    erd = Digraph('ERD', format='png')
    erd.attr(rankdir='LR', splines='polyline', nodesep='0.8', ranksep='2.0')
    erd.attr('node', shape='plaintext')
    erd.attr('edge', fontsize='10', fontname='Arial')
    
    # Define entity tables with their attributes
    entities = {
        'Article': {
            'color': '#B4D7E5',
            'attributes': [
                ('PK', 'article_id', 'VARCHAR'),
                ('', 'title', 'VARCHAR'),
                ('', 'author', 'VARCHAR'),
                ('', 'date', 'DATE'),
                ('', 'volume_number', 'INT'),
                ('', 'issue_number', 'VARCHAR'),
                ('', 'pages', 'VARCHAR'),
                ('', 'monograph_publishers', 'VARCHAR'),
                ('', 'archival_holding', 'VARCHAR'),
                ('', 'archival_location', 'VARCHAR'),
                ('', 'cost', 'VARCHAR'),
                ('', 'permission', 'VARCHAR'),
                ('', 'permission_acknowledgement', 'VARCHAR'),
                ('', 'permission_statements', 'VARCHAR'),
                ('', 'acquisitions', 'VARCHAR'),
                ('', 'document_intro', 'TEXT'),
                ('', 'transcripts', 'TEXT'),
                ('FK', 'group_reprint_id', 'VARCHAR'),
                ('FK', 'publisher_location', 'VARCHAR'),
                ('FK', 'publication', 'VARCHAR')
            ]
        },
        'Publication': {
            'color': '#F4D9B0',
            'attributes': [
                ('PK', 'publication', 'VARCHAR'),
                ('FK', 'publisher_location', 'VARCHAR')
            ]
        },
        'Location': {
            'color': '#C8E6C9',
            'attributes': [
                ('PK', 'publisher_location', 'VARCHAR')
            ]
        },
        'Images': {
            'color': '#E1BEE7',
            'attributes': [
                ('PK', 'object_id', 'VARCHAR'),
                ('', 'image_file', 'VARCHAR'),
                ('', 'image_parent_id', 'VARCHAR'),
                ('', 'image_object_location', 'VARCHAR'),
                ('', 'image_display_template', 'VARCHAR'),
                ('', 'image_description', 'TEXT'),
                ('FK', 'article_id', 'VARCHAR')
            ]
        },
        'Reprints': {
            'color': '#FFECB3',
            'attributes': [
                ('PK', 'group_reprint_id', 'VARCHAR'),
                ('', 'reprint_type', 'VARCHAR'),
                ('', 'reprint_order', 'INT')
            ]
        },
        'Trope': {
            'color': '#FFCDD2',
            'attributes': [
                ('PK', 'trope_id', 'VARCHAR'),
                ('', 'trope_label', 'VARCHAR')
            ]
        },
        'Article_Trope': {
            'color': '#FFE0E0',
            'attributes': [
                ('PK,FK', 'article_id', 'VARCHAR'),
                ('PK,FK', 'trope_id', 'VARCHAR')
            ]
        }
    }
    
    # Create HTML-like table for each entity
    for entity_name, entity_data in entities.items():
        # Build HTML table
        html = f'''<
<TABLE BORDER="2" CELLBORDER="1" CELLSPACING="0" CELLPADDING="6">
  <TR><TD BGCOLOR="{entity_data['color']}" COLSPAN="3"><FONT POINT-SIZE="14"><B>{entity_name}</B></FONT></TD></TR>
'''
        
        for key_type, attr_name, data_type in entity_data['attributes']:
            if 'PK' in key_type:
                key_icon = '🔑 '
            elif 'FK' in key_type:
                key_icon = '🔗 '
            else:
                key_icon = '   '
            
            html += f'  <TR><TD ALIGN="LEFT">{key_icon}</TD><TD ALIGN="LEFT"><B>{attr_name}</B></TD><TD ALIGN="LEFT"><I>{data_type}</I></TD></TR>\n'
        
        html += '</TABLE>>'
        
        erd.node(entity_name, label=html)
    
    # Define relationships using proper crow's foot notation
    # Format: (source, target, source_card, target_card, label)
    # Cardinality: '1' = one, 'N' = many (crow's foot)
    relationships = [
        ('Article', 'Publication', 'N', '1', 'published in'),
        ('Article', 'Location', 'N', '1', 'published at'),
        ('Publication', 'Location', 'N', '1', 'located at'),
        ('Article', 'Images', '1', 'N', 'has'),
        ('Article', 'Reprints', 'N', '1', 'belongs to'),
        ('Article', 'Article_Trope', '1', 'N', ''),
        ('Trope', 'Article_Trope', '1', 'N', ''),
    ]
    
    # Add edges with proper crow's foot notation
    for source, target, source_card, target_card, label in relationships:
        # Determine arrow styles based on cardinality
        if target_card == 'N':
            arrowhead = 'crow'
        else:
            arrowhead = 'none'
            
        if source_card == 'N':
            arrowtail = 'crow'
        else:
            arrowtail = 'none'
        
        # Create label with cardinality
        edge_label = f'{label}\n({source_card}:{target_card})' if label else f'({source_card}:{target_card})'
        
        erd.edge(source, target, xlabel=edge_label, 
                arrowhead=arrowhead, arrowtail=arrowtail, dir='both',
                penwidth='1.5')
    
    # Add title and legend
    erd.attr(label='\n\nEntity-Relationship Diagram\\nLone Woman Historical Newspaper Collection\\n\\n' +
                   '🔑 = Primary Key    🔗 = Foreign Key    Crow\'s Foot = Many    Line = One',
             fontsize='16', labelloc='t', fontname='Arial Bold')
    
    # Render the diagram
    try:
        erd.render(output_file, cleanup=True, format='png')
        erd.render(output_file + '_svg', cleanup=True, format='svg')
        print(f"✓ Enhanced ERD successfully generated!")
        print(f"  - PNG: {output_file}.png")
        print(f"  - SVG: {output_file}_svg.svg")
        
        # Print summary statistics
        print(f"\n📊 Dataset Statistics:")
        print(f"  - Total records (images): {len(df)}")
        print(f"  - Unique articles: {df['article_id'].nunique()}")
        print(f"  - Unique images: {df['object_id'].nunique()}")
        print(f"  - Unique publications: {df['publication'].nunique()}")
        print(f"  - Unique locations: {df['publisher_location'].nunique()}")
        print(f"  - Unique reprint groups: {df['group_reprint_id'].nunique()}")
        
        # Count tropes
        all_tropes = set()
        for trope_str in df['tropes'].dropna():
            tropes = [t.strip() for t in str(trope_str).split(';')]
            all_tropes.update(tropes)
        print(f"  - Unique tropes: {len(all_tropes)}")
        
        # Calculate average images per article
        avg_images = len(df) / df['article_id'].nunique()
        print(f"  - Average images per article: {avg_images:.1f}")
        
        # Show reprint distribution
        print(f"\n📰 Reprint Type Distribution:")
        reprint_counts = df.groupby('reprint_type')['article_id'].nunique()
        for reprint_type, count in reprint_counts.items():
            print(f"  - {reprint_type}: {count} articles")
        
    except Exception as e:
        print(f"Error rendering ERD: {e}")
        import traceback
        traceback.print_exc()
        return None
    
    return erd

if __name__ == "__main__":
    csv_file = sys.argv[1] if len(sys.argv) > 1 else "/mnt/user-data/uploads/lonewoman_complete_metadata_example.csv"
    create_enhanced_erd(csv_file)
