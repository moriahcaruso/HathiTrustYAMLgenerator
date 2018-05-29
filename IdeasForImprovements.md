# Ideas for improvement
- Currently, the following lines must be removed from YAML files describing items for which image files have remained uncompressed:
   - image_compression_date
   - image_compression_tool
   - image_compression_agent  
   *The data entry template and script could be modified so that lines regarding compression date, information, etc., are not output in YAML files if images are uncompressed.*
- As [noted](https://github.com/ries07uw/HathiTrustYAMLgenerator/blob/master/HowTo.md#note), support for books read from right to left is limited. Improving capability to generate YAML files for such items is a potential area for improvement in the Python script.
- As of this writing, it is not clear to [me](https://github.com/briesenberg07) exactly how page tags show up and function for users in the HathiTrust. A better understanding of the way that applying page tags to image files affects the presentation of items in the HathiTrust user interface would allow for providing more specific and helpful guidance on how page images should be tagged.
