# frozen_string_literal: true

module Jekyll
  module TextFilters
    # Source essay text (document_intro, source notes) uses an inconsistent
    # number of newlines between paragraphs (2-3, with stray spaces). Split
    # on any blank-line run and wrap each paragraph in <p>, rather than
    # relying on newline_to_br, which turns every stray extra newline into
    # its own visible blank line.
    def paragraphize(input, css_class = "")
      return "" if input.nil?
      paragraphs = input.to_s.strip.split(/\n[ \t]*\n/)
      class_attr = css_class.empty? ? "" : " class=\"#{css_class}\""
      paragraphs.map { |p| "<p#{class_attr}>#{p.strip}</p>" }.join
    end
  end
end

Liquid::Template.register_filter(Jekyll::TextFilters)
