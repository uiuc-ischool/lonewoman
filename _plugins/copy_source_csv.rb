# frozen_string_literal: true

# Copies the raw master metadata CSV from _data/ into the built site
# verbatim, so the Data page's "Complete Metadata" download is guaranteed
# to be byte-identical to _data/<metadata>.csv rather than a Liquid-
# regenerated (and potentially re-quoted or field-limited) copy of it.
module CopySourceCSV
  class RenamedStaticFile < Jekyll::StaticFile
    def initialize(site, base, src_dir, src_name, dest_dir)
      super(site, base, src_dir, src_name)
      @dest_dir = dest_dir
    end

    def destination(dest)
      File.join(dest, @dest_dir, name)
    end
  end

  class Generator < Jekyll::Generator
    safe true

    def generate(site)
      csv_name = "#{site.config['metadata']}.csv"
      src_path = File.join(site.source, '_data', csv_name)
      return unless File.exist?(src_path)

      site.static_files << RenamedStaticFile.new(site, site.source, '_data', csv_name, 'assets/data')
    end
  end
end
